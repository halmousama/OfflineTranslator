from customtkinter import *
from layoutComponents.theme_manager import change_theme
import os
from tkinter import filedialog
from tkinter import messagebox

def open_file():
    # Prompt the user to open a file
    file_path = filedialog.askopenfilename(
        title="Select a file"
    )
    
    # Check if a file was selected
    if file_path:
        messagebox.showinfo("File Selected", f"You selected: {file_path}")
        # Process the file (for example, open it or display in the app)
    else:
        messagebox.showwarning("No File Selected", "Please select a file.")


def file_option(option):
    if option.get() == "Open":
        open_file()
    elif option == "Save":
        print("Save")
    elif option == "Save as":
        print("Save as")
    elif option == "Exit":
        os._exit(0)
    option.set("File")



def create_menu_bar(master):
    menu_bar_container = CTkFrame(master=master, height=30)
    menu_bar_container.pack(padx=5, pady=5, fill="both", expand=False)
    
    file_menu = CTkOptionMenu(
        master=menu_bar_container, values=["Open", "Save", "Save as", "Exit"], height=20, width=55, command=lambda value: file_option(file_menu)
    )
    file_menu.grid(row=0, column=0, padx=2, pady=10, sticky="ew")
    file_menu.set("File")

    edit_menu = CTkOptionMenu(
        master=menu_bar_container, values=["Undo", "Redo", "Cut", "Copy", "Paste"], height=20, width=55
    )
    edit_menu.grid(row=0, column=1, padx=2, pady=10, sticky="ew")
    edit_menu.set("Edit")

    view_menu = CTkOptionMenu(
        master=menu_bar_container, values=["Zoom in", "Zoom out", "Reset Zoom"], height=20, width=55
    )
    view_menu.grid(row=0, column=2, padx=2, pady=10, sticky="ew")
    view_menu.set("View")

    help_menu = CTkOptionMenu(
        master=menu_bar_container, values=["About"], height=20, width=55
    )
    help_menu.grid(row=0, column=3, padx=2, pady=10, sticky="ew")
    help_menu.set("Help")

    # Theme selection menu
    app_theme = CTkOptionMenu(
        master=menu_bar_container,
        values=["System", "Dark", "Light"],
        height=20,
        width=55,
        command=lambda value: change_theme(app_theme.get()),
    )
    app_theme.grid(row=0, column=4, padx=0, pady=10, sticky="ew")
    app_theme.set("Theme")
    
    return menu_bar_container