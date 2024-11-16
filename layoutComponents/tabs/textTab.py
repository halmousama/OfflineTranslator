from customtkinter import CTkFrame, CTkTextbox
from awesometkinter.bidirender import add_bidi_support
from layoutComponents.translateUtils import translate 
from layoutComponents.config import *

def text_tab_layout(master):
    languages_container = CTkFrame(master=master)
    languages_container.pack(padx=10, pady=10, fill="both", expand=True)
    from_text = CTkTextbox(languages_container, font=("Monospace", 14), wrap="word", width=textBoxWidth)
    from_text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    to_text = CTkTextbox(languages_container, font=("Monospace", 14), wrap="word", width=textBoxWidth)
    to_text.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
    add_bidi_support(from_text)
    add_bidi_support(to_text)
    from_text.bind("<space>", lambda event: translate(from_text, to_text), add="+")
    from_text.bind("<Return>", lambda event: translate(from_text, to_text), add="+")