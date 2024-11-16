from customtkinter import CTkSlider
from layoutComponents.config import textBoxWidth
def scallingWindow(x):
    global textBoxWidth
    textBoxWidth = x
    # create_tabs(window)
def scallingSliderLayout(master):
    scalling=CTkSlider(master=master,from_=300,to=600, command=scallingWindow)
    scalling.pack(padx=10, pady=10, fill="both", expand=True)
 