from customtkinter import CTkFrame, CTkButton, CTkOptionMenu, CTkImage
from PIL import Image
import layoutComponents.config as config

def language_buttons(master):

    language_buttons_container = CTkFrame(master=master)
    language_buttons_container.pack(padx=10, pady=10, fill="both", expand=True)

    config.source_language_container = CTkFrame(master=language_buttons_container, width=config.textBoxWidth + 100)
    config.source_language_container.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    spacing = CTkFrame(master=language_buttons_container, width=config.textBoxWidth)
    spacing.grid(row=0, column=1, padx=10, pady=10)
    img = CTkImage(light_image=Image.open("/home/ous/Documents/vscode/PYTHON/Translator_App/img/double-fleche.png"), dark_image=Image.open("/home/ous/Documents/vscode/PYTHON/Translator_App/img/double-fleche.png"))
    img_btn = CTkButton(spacing, image=img, text="", width=30, bg_color="transparent", fg_color="transparent", hover_color="#2f2f2f", border_width=0, command=lambda: inverse_language())
    img_btn.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
    config.target_language_container = CTkFrame(master=language_buttons_container)
    config.target_language_container.grid(row=0, column=2, padx=10, pady=10, sticky="e")

    config.language_buttons_source.extend([
        CTkButton(config.source_language_container, text="English", width=60),
        CTkButton(config.source_language_container, text="Arabic", width=60),
        CTkButton(config.source_language_container, text="French", width=60),
        CTkOptionMenu(config.source_language_container, values=["Other...", "Espanol", "Hindi", "Italiano", "Portugues", "Roma"], width=60)
    ])

    for i, button in enumerate(config.language_buttons_source):
        button.grid(row=0, column=i, padx=10, pady=10, sticky="nsew")

    config.language_buttons_target.extend([
        CTkButton(config.target_language_container, text="English", width=60),
        CTkButton(config.target_language_container, text="Arabic", width=60),
        CTkButton(config.target_language_container, text="French", width=60),
        CTkOptionMenu(config.target_language_container, values=["Other...", "Espanol", "Hindi", "Italiano", "Portugues", "Roma"], width=60)
    ])

    for i, button in enumerate(config.language_buttons_target):
        button.grid(row=0, column=i, padx=10, pady=10, sticky="nsew")

    change_button_color("src", config.language_buttons_source[0])
    change_button_color("tgt", config.language_buttons_target[1])
    for i in range(len(config.language_buttons_source)):
        config.language_buttons_source[i].bind("<Button-1>", lambda event, index=i: change_button_color("src", config.language_buttons_source[index]))
        config.language_buttons_target[i].bind("<Button-1>", lambda event, index=i: change_button_color("tgt", config.language_buttons_target[index]))


def langNameToLangCode(langName):
    return {
        "English": "en",
        "Arabic": "ar",
        "French": "fr",
        "Espanol": "es",
        "Hindi": "hi",
        "Italiano": "it",
        "Portugues": "pt",
        "Roma": "ro"
    }.get(langName, "other")
def langCodeToLangName(langCode):
    return {
        "en": "English",
        "ar": "Arabic",
        "fr": "French",
        "es": "Espanol",
        "hi": "Hindi",
        "it": "Italiano",
        "pt": "Portugues",
        "ro": "Roma"
    }.get(langCode, "other")
def langNameToButton(mode,langName):
    if mode == "src":
        return {
            "English": config.language_buttons_source[0],
            "Arabic": config.language_buttons_source[1],
            "French": config.language_buttons_source[2]
        }.get(langName, "other")
    elif mode == "tgt":
        return {
            "English": config.language_buttons_target[0],
            "Arabic": config.language_buttons_target[1],
            "French": config.language_buttons_target[2]
        }.get(langName, "other")
def change_language(mode, language):
    if mode == "src":
        config.source_language = language
    elif mode == "tgt":
        config.target_language = language

def inverse_language():
    config.source_language, config.target_language = config.target_language, config.source_language
    change_button_color("src",langNameToButton("src",langCodeToLangName(config.source_language)))
    change_button_color("tgt",langNameToButton("tgt",langCodeToLangName(config.target_language)))

def change_button_color( mode, button):
    # print("mode: ", mode, "\nLangs before: ", config.source_language, config.target_language)
    
    change_language(mode, langNameToLangCode(button.cget("text")))
    # print("Langs after: ", config.source_language, config.target_language)
    if mode == "src":
        for b in config.language_buttons_source:
            if b == button:
                b.configure(fg_color="green", text_color="white")
            else:
                b.configure(fg_color="gray55", text_color="black")
    elif mode == "tgt":
        for b in config.language_buttons_target:
            if b == button:
                b.configure(fg_color="green", text_color="white")
            else:
                b.configure(fg_color="gray55", text_color="black")

