Absolutely, here's the translated markdown code for your README.md:

# Offline Translator Desktop App


## Overview

This desktop application allows offline translation of text, images, and documents. It currently supports English, French, and Arabic, with the ability to expand to additional languages by installing corresponding language models. The app also provides light and dark themes, which adapt to your system theme for a comfortable experience.

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/4245cc88-8cfb-4344-a058-b76aac12b7d6"></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/d1f9726b-8319-4cab-be27-558057e84407"></td>
  </tr>
</table>

## Features

* **Multi-Language Support**: Translate between English, French, and Arabic (expandable to other languages).
* **Multi-Input Translation**:
    * Plain text
    * Images
    * Document files
* **Efficient Processing**: Translation operations run in a separate process to maintain smooth app performance.
* **Customizable Themes**: Automatically switches between light and dark modes based on your system settings.

## Installation

To install the application and its dependencies, follow these steps:

### 1. Set Up Virtual Environment

Create a virtual environment in the directory where your app will reside:

```bash
python -m venv myapp_env
```

### 2. Activate the Virtual Environment

* **Windows:**

```bash
myapp_env\Scripts\activate
```

* **Linux/macOS:**

```bash
source myapp_env/bin/activate
```

### 3. Install Dependencies

Install the necessary libraries:

```bash
pip install customtkinter Pillow awesometkinter textract transformers
```

## Usage

### 1. Choose Input Type

Select the type of input for translation:

* Text
* Image
* Document

### 2. Translate Offline

The app uses machine learning models for offline translation. You can install additional models for other languages as needed.

### 3. Theme Adaptation

The app automatically adapts to your system's light or dark theme preferences.

## Customization

* **Language Models**: To expand support for other languages, install the required language models.
* **Theme Customization**: The app switches between light and dark themes based on your system settings.

## Test Users

![Screenshot: translate an image](https://github.com/user-attachments/assets/0a58801f-9aca-41ea-88c7-8be5cc57f14e)

Test the app with the following configurations to ensure it works as expected:

* **Text Translation**: Test with various plain text inputs.
* **Image Translation**: Test with images in formats supported by PIL (e.g., PNG, JPEG).
* **Document Translation**: Test with PDF, Word, and other supported document types.
* **Theme Adaptation**: Verify automatic switching between light and dark themes based on system preferences.

## Contributing

We welcome contributions to improve the app! To contribute:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.

## License

This project is open-source and distributed under the MIT License.

## Acknowledgements

Special thanks to the creators of the following libraries for their contributions:

* Tkinter
* customtkinter
* transformers
* textract
* Pillow
* awesometkinter
