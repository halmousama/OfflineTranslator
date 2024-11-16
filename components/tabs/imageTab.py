import os
import threading
from tkinter import filedialog
from PIL import Image, UnidentifiedImageError
from customtkinter import CTkFrame, CTkTextbox, CTkLabel, CTkImage
from awesometkinter.bidirender import add_bidi_support, render_text
import textract
import components.config as conf
from components.translateUtils import translate_from_image

from_text = None
to_text = None


def image_tab_layout(master):
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
        light_image=Image.open(conf.img_path),
        dark_image=Image.open(conf.img_path),
        size=(conf.textBoxWidth, int(conf.textBoxWidth / 2)),
    )
    img_btn = CTkLabel(master=languages_container, text="", image=img)
    img_btn.grid(row=0, column=0, padx=10, pady=4, sticky="nsew")
    img_btn.bind("<Button-1>", lambda e: upload_image(img_btn))

    to_text = CTkTextbox(
        languages_container,
        font=("Monospace", 14),
        wrap="word",
        width=conf.textBoxWidth,
    )
    to_text.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

    add_bidi_support(from_text)
    add_bidi_support(to_text)


def upload_image(img_btn):
    conf.img_path = filedialog.askopenfilename()
    print(f"Selected image: {conf.img_path}")

    try:
        # Check if the file exists
        if not os.path.isfile(conf.img_path):
            raise FileNotFoundError(f"File not found: {conf.img_path}")

        # Validate the file format
        valid_extensions = (".png", ".jpg", ".jpeg", ".bmp", ".gif")
        if not conf.img_path.lower().endswith(valid_extensions):
            raise ValueError("Selected file is not a valid image format.")

        # Open the image
        img = CTkImage(
            light_image=Image.open(conf.img_path),
            dark_image=Image.open(conf.img_path),
            size=(conf.textBoxWidth, int(conf.textBoxWidth / 2)),
        )
        img_btn.configure(image=img)
        extraxt_text()
    except FileNotFoundError as e:
        print(e)
    except UnidentifiedImageError as e:
        print(f"Error: File is not a valid image. {e}")
    except Exception as e:
        print(f"Failed to load image: {e}")


def translate_thread(text):
    global to_text
    try:
        tranlated_text = translate_from_image(text)
        rendering_text = render_text(tranlated_text)
        to_text.delete("1.0", "end")
        to_text.insert("1.0", rendering_text)
    except Exception as e:
        print(f"Error translating text: {e}")


def extraxt_text():
    global from_text, to_text
    try:
        text = textract.process(conf.img_path)
        text = text.decode("utf-8")  # Decode bytes to string
        # print(text)
        from_text.insert("1.0", text)
        threading.Thread(target=translate_thread, args=(text,), daemon=True).start()
    except Exception as e:
        print(f"Error extracting text: {e}")
