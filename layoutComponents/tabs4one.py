from customtkinter import CTkTabview
from awesometkinter.bidirender import add_bidi_support, render_text
from layoutComponents.tabs.textTab import text_tab_layout
from layoutComponents.tabs.imageTab import image_tab_layout
# from layoutComponents.tabs.audioTab import audio_tab_layout
from layoutComponents.tabs.documentTab import document_tab_layout


def create_tabs(master):
    tabs = CTkTabview(master=master)
    tabs.pack(padx=10, pady=10, fill="both", expand=True)

    add_bidi_support(tabs)

    text_tab = tabs.add("Text")
    image_tab = tabs.add("Image")
    audio_tab = tabs.add("Audio")
    document_tab = tabs.add("Document")

    tabs.set("Text")

    text_tab_layout(text_tab)

    image_tab_layout(image_tab)

    document_tab_layout(document_tab)

    return tabs
