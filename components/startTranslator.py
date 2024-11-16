from customtkinter import CTk, set_appearance_mode, set_default_color_theme
from components.tabs4one import create_tabs
from components.languagesButtons import language_buttons
from components.config import *


def main():
    set_appearance_mode("system")
    set_default_color_theme("blue")

    window = CTk()
    window.title("Offline Translator")

    language_buttons(window)

    create_tabs(window)

    window.mainloop()
