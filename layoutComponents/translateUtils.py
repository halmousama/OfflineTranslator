import threading
import typing as t
from transformers import MarianMTModel, MarianTokenizer
from awesometkinter.bidirender import render_text
import layoutComponents.config as config

model_mappings = {
    ("en", "ar"): "Helsinki-NLP/opus-mt-en-ar",
    ("ar", "en"): "Helsinki-NLP/opus-mt-ar-en",
    ("en", "fr"): "Helsinki-NLP/opus-mt-en-fr",
    ("fr", "en"): "Helsinki-NLP/opus-mt-fr-en",
    ("ar", "fr"): "Helsinki-NLP/opus-mt-ar-fr",
    ("fr", "ar"): "Helsinki-NLP/opus-mt-fr-ar",
}
# Function to translate textdef translate_text(text):
def translate_text(text):
    model_name = model_mappings.get((config.source_language, config.target_language))
    if not model_name:
        raise ValueError(f"Translation from {config.source_language} to {config.target_language} is not supported.")
    
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    
    # Split the text into lines to preserve line breaks
    lines = text.split("\n")
    
    # Tokenize and translate each line separately, handling empty lines
    translated_lines = []
    for line in lines:
        if line.strip() == "":  # Check if the line is empty or just whitespace
            translated_lines.append("")  # Preserve empty lines as is
        else:
            inputs = tokenizer(line, return_tensors="pt", padding=True, truncation=True)
            translated = model.generate(**inputs)
            translated_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
            translated_lines.append(translated_text[0])  # Append translated line
    
    # Join the translated lines with newlines
    return "\n".join(translated_lines)

def translate(from_text, to_text):
    config.stop_translation_thread = True

    if threading.active_count() > 1:
        return

    def translate_thread():
        config.stop_translation_thread = False

        to_text.delete("1.0", "end")
        try:
            input_text = from_text.get("1.0", "end-1c").strip()
            translated_text = translate_text(input_text)
            translated_text = render_text(translated_text)
            to_text.insert("1.0", translated_text)
        except ValueError as e:
            print(e)
        finally:
            config.stop_translation_thread = True

    threading.Thread(target=translate_thread).start()

