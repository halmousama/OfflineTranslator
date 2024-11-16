from customtkinter import CTkFrame, CTkTextbox
from awesometkinter.bidirender import add_bidi_support
from components.translateUtils import translate, TranslationState
from components.config import *


def text_tab_layout(master):
    languages_container = CTkFrame(master=master)
    languages_container.pack(padx=10, pady=10, fill="both", expand=True)
    from_text = CTkTextbox(
        languages_container, font=("Monospace", 14), wrap="word", width=textBoxWidth
    )
    from_text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    to_text = CTkTextbox(
        languages_container, font=("Monospace", 14), wrap="word", width=textBoxWidth
    )
    to_text.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
    add_bidi_support(from_text)
    add_bidi_support(to_text)

    # Initialize translation state
    translation_state = TranslationState()

    # Bind translation triggers
    def on_key(event):
        if translation_state.is_ready:
            translate(from_text, to_text, translation_state)

    from_text.bind("<space>", on_key, add="+")
    from_text.bind("<Return>", on_key, add="+")
