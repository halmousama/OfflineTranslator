from customtkinter import set_appearance_mode, set_default_color_theme
import layoutComponents.config as config

def initialize_theme():
    set_appearance_mode("system")  # dark/light system mode
    set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
 
def change_theme(theme):
    config.theme = theme 