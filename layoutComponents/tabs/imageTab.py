from customtkinter import CTkFrame, CTkTextbox, CTkLabel, CTkImage
from awesometkinter.bidirender import add_bidi_support
from PIL import Image
from layoutComponents.config import *

def image_tab_layout(master):
    languages_container = CTkFrame(master=master)
    languages_container.pack(padx=10, pady=10, fill="both", expand=True)
    from_text = CTkTextbox(languages_container, font=("Monospace", 14), wrap="word", width=textBoxWidth)
    from_text.grid(row=1, column=0, padx=10, pady=4, sticky="nsew")
    img = CTkImage(light_image=Image.open("img/uploadImg.png"), dark_image=Image.open("img/uploadImg.png"), size=(textBoxWidth, int(textBoxWidth * (3 / 4))))
    img_btn = CTkLabel(master=languages_container, text="", image=img)
    img_btn.grid(row=0, column=0, padx=10, pady=4, sticky="nsew")
    to_text = CTkTextbox(languages_container, font=("Monospace", 14), wrap="word", width=textBoxWidth)
    to_text.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")
    add_bidi_support(from_text)
    add_bidi_support(to_text)