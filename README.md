## Project Title: Simple UI for ChatGPT 3.5 Turbo with System/Message Prompt Access

This project provides a simple and interactive Python-based user interface (UI) for OpenAI's GPT-3.5 Turbo model. It allows you to enter both system prompts and user messages to guide the AI's responses, making it easier to experiment with the capabilities of the model.

## Getting Started

The following instructions will guide you on how to run this project on your local machine.

## Prerequisites

You need to have the following installed on your local machine:

Python 3
openai, tkinter, and pyperclip Python libraries. You can install these libraries using pip:
pip install openai tkinter pyperclip

An API key from OpenAI. You can get it from the OpenAI website after registration.
Usage

Clone the repository or download the project files.
Replace the openai.api_key variable in the script with your own API key.
Run the script using Python.
Application Features

## The application has the following main features:

API Key Entry: Allows the user to input their OpenAI API key.
Prompt Entry: Allows the user to enter a system prompt that guides the AI's responses.
Message Entry: Allows the user to enter a message which is added to the list of system and user messages used to guide the AI's response.
Output Box: Displays the AI's response.
Control Buttons:
Submit Key: Submits the API Key and checks its validity.
Submit Prompt: Submits the system prompt and initiates the AI's response generation.
Submit Message: Submits the user's message and initiates the AI's response generation.
Copy Output: Copies the contents of the output box to the clipboard.
Clear Output: Clears the contents of the output box.

## Built with

Python
Tkinter
OpenAI

## Note

This application requires a valid API key from OpenAI, which is used to interact with the OpenAI GPT-3.5 Turbo model for text generation. The performance of the application greatly depends on the provided API key.

## License

This project is open source and available under the MIT License.

## Disclaimer

This application is not an official product by OpenAI. It is developed for educational purposes and should not be used for malicious purposes.

## Contributing

Contributions, issues, and feature requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
