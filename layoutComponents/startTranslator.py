from customtkinter import CTk, set_appearance_mode, set_default_color_theme
from layoutComponents.tabs4one import create_tabs
from layoutComponents.languagesButtons import language_buttons
from layoutComponents.config import *

def main():
    set_appearance_mode("system") 
    set_default_color_theme("blue")
    
    window = CTk()
    window.title("Offline Translator")
    
    language_buttons(window)
    
    create_tabs(window)
    
    window.mainloop()

