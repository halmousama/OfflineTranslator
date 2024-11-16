import os
import threading
from customtkinter import CTkFrame, CTkImage, CTkLabel, CTkTextbox
import components.config as conf
from components.translateUtils import translate_from_image
from PIL import Image
from tkinter import filedialog
from awesometkinter.bidirender import add_bidi_support, render_text
import textract

from_text = None
to_text = None


def document_tab_layout(master):
    global from_text, to_text

    languages_container = CTkFrame(master=master)
    languages_container.pack(padx=10, pady=10, fill="both", expand=True)

    from_text = CTkTextbox(
        languages_container,
        font=("Monospace", 14),
        wrap="word",
        width=conf.textBoxWidth,
    )
    from_text.grid(row=1, column=0, padx=10, pady=4, sticky="nsew")

    img = CTkImage(
        light_image=Image.open("img/uploadImg.png"),
        dark_image=Image.open("img/uploadImg.png"),
        size=(conf.textBoxWidth, int(conf.textBoxWidth / 2)),
    )
    img_btn = CTkLabel(master=languages_container, text="", image=img)
    img_btn.grid(row=0, column=0, padx=10, pady=4, sticky="nsew")
    img_btn.bind("<Button-1>", lambda e: upload_document())

    to_text = CTkTextbox(
        languages_container,
        font=("Monospace", 14),
        wrap="word",
        width=conf.textBoxWidth,
    )
    to_text.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

    add_bidi_support(from_text)
    add_bidi_support(to_text)


def translate_thread(text):
    global to_text
    try:
        tranlated_text = translate_from_image(text)
        rendering_text = render_text(tranlated_text)
        to_text.delete("1.0", "end")
        to_text.insert("1.0", rendering_text)
    except Exception as e:
        print(f"Error translating text: {e}")


def upload_document():

    file_path = filedialog.askopenfilename()

    try:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        textE = textract.process(file_path).decode("utf-8")
        from_text.insert("1.0", textE)
        threading.Thread(target=translate_thread, args=(textE,), daemon=True).start()
    except Exception as e:
        print(f"Error extracting text: {e}")
