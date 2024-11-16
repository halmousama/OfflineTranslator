import threading
from transformers import MarianMTModel, MarianTokenizer
from awesometkinter.bidirender import render_text
import components.config as config

model_mappings = {
    ("en", "ar"): "Helsinki-NLP/opus-mt-en-ar",
    ("ar", "en"): "Helsinki-NLP/opus-mt-ar-en",
    ("en", "fr"): "Helsinki-NLP/opus-mt-en-fr",
    ("fr", "en"): "Helsinki-NLP/opus-mt-fr-en",
    ("ar", "fr"): "Helsinki-NLP/opus-mt-ar-fr",
    ("fr", "ar"): "Helsinki-NLP/opus-mt-fr-ar",
}


class TranslationState:
    def __init__(self):
        self.is_ready = True
        self.last_text = ""


def translate_text(text):
    model_name = model_mappings.get((config.source_language, config.target_language))
    if not model_name:
        raise ValueError(
            f"Translation from {config.source_language} to {config.target_language} is not supported."
        )

    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    lines = text.split("\n")
    translated_lines = []
    for line in lines:
        if line.strip() == "":
            translated_lines.append("")
        else:
            inputs = tokenizer(line, return_tensors="pt", padding=True, truncation=True)
            translated = model.generate(**inputs)
            translated_text = tokenizer.batch_decode(
                translated, skip_special_tokens=True
            )
            translated_lines.append(translated_text[0])

    return "\n".join(translated_lines)


def translate(from_text, to_text, state):
    current_text = from_text.get("1.0", "end-1c").strip()

    # Skip if text hasn't changed
    if current_text == state.last_text:
        return

    # Update last_text to current input
    state.last_text = current_text

    # If a translation is already in progress, skip
    if not state.is_ready:
        return

    def translate_thread():
        state.is_ready = False
        try:
            translated_text = translate_text(current_text)
            translated_text = render_text(translated_text)
            to_text.delete("1.0", "end")
            to_text.insert("1.0", translated_text)
        except ValueError as e:
            print(e)
        finally:
            state.is_ready = True

    threading.Thread(target=translate_thread, daemon=True).start()


# function to run thread to translate text from image
def translate_from_image(from_text):
    model_name = model_mappings.get((config.source_language, config.target_language))
    if not model_name:
        raise ValueError(
            f"Translation from {config.source_language} to {config.target_language} is not supported."
        )

    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    lines = from_text.split("\n")
    translated_lines = []
    for line in lines:
        if line.strip() == "":
            translated_lines.append("")
        else:
            inputs = tokenizer(line, return_tensors="pt", padding=True, truncation=True)
            translated = model.generate(**inputs)
            translated_text = tokenizer.batch_decode(
                translated, skip_special_tokens=True
            )
            translated_lines.append(translated_text[0])

    return "\n".join(translated_lines)
