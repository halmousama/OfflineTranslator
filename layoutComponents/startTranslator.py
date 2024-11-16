from customtkinter import CTk
from layoutComponents.menu_bar import create_menu_bar
from layoutComponents.tabs4one import create_tabs
from layoutComponents.theme_manager import initialize_theme
from layoutComponents.languagesButtons import language_buttons
# from layoutComponents.scallingSlider import scallingSliderLayout
from layoutComponents.config import *

def main():
    initialize_theme()
    
    window = CTk()
    window.title("Offline Translator")
    
    create_menu_bar(window)
    
    # scallingSliderLayout(window)
    
    language_buttons(window)
    
    create_tabs(window)
    
    window.mainloop()

