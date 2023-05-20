## Simple UI for ChatGPT 3.5 Turbo with System/Message Prompt Access

This project provides a simple and interactive Python-based user interface (UI) for OpenAI's GPT-3.5 Turbo model. It allows you to enter both system prompts and user messages to guide the AI's responses, making it easier to experiment with the capabilities of the model.

Python release download:
- https://github.com/itsRevela/Simple-GPT-3.5-Turbo-Desktop-Interface/blob/master/GPT-Interface-v1.02-public.py

Windows release download: 
- https://github.com/itsRevela/Simple-GPT-3.5-Turbo-Desktop-Interface/blob/master/dist/GPT-Interface-v1.02-public.exe

## Example
![Program demo](https://github.com/itsRevela/Simple-GPT-3.5-Turbo-Desktop-Interface/blob/d8cd4ea57da1d0bf1d7424b7368da25e0d6f2f98/demo.png)


## Getting Started

The following instructions will guide you on how to run this project on your local machine.

## Usage

- Clone the repository or download the project files.
- Replace the openai.api_key variable in the script with your own API key.
- Run the script using Python.

## Requirements

- An API key from OpenAI. You can get it from the OpenAI website after registration.
- Python 3.7 or higher (I compiled this program with Python 3.11.3)
- openai module
- tkinter module
- pyperclip module

## Installation Guide

### Step 1: Installing Python

1. Visit the official Python website at https://www.python.org/.
2. Hover over the Downloads tab and click on Python 3.x.x (or the latest version available).
3. Download the installation file, run it, and follow the instructions in the installer. Make sure to check the box that asks if you want to 'Add Python 3.x to PATH' before you click on 'Install Now'.

### Step 2: Setting Up a Virtual Python Environment

It's a good practice to create a virtual environment for each of your Python projects. Here's how you can do it:

1. Open your command prompt (Windows) or terminal (MacOS, Linux).
2. Navigate to the directory where you want your project to live using the 'cd' command followed by your desired directory.
3. Once you're in the desired directory, run the following command to create a virtual environment:

   python3 -m venv env

4. Activate the virtual environment:

   - Windows:
     .\env\Scripts\activate

   - MacOS/Linux:
     source env/bin/activate

You should now see `(env)` before the path in your command prompt or terminal. This means that the virtual environment is active.

### Step 3: Installing the Dependencies

Now you need to install the dependencies required for this project:

1. Ensure your virtual environment is active. If it's active, you'll see `(env)` on your command prompt or terminal.
2. Run the following command to install the necessary Python packages:

   pip install openai tkinter pyperclip

### Step 4: Running the Program

With Python and the necessary packages installed, you can now run the program:

1. Download the Python file and place it in the same directory as your virtual environment.
2. In your terminal, ensure your virtual environment is active, navigate to the directory where your Python file is located if you're not already there.
3. Run the program with the following command:

   python file_name.py

   Replace "file_name.py" with the name of your Python script.

Please replace the OpenAI API key in the code with your actual API key to make the program work correctly.

And that's it! You've set up and run the Python program.

## The application has the following main features:

Text input:
- API Key Entry: Allows the user to input their OpenAI API key.
- Prompt Entry: Allows the user to enter a system prompt that guides the AI's responses.
- Message Entry: Allows the user to enter a message which is added to the list of system and user messages used to guide the AI's response.
- Output Box: Displays the AI's response.

Control Buttons:
- Submit Key: Submits the API Key and checks its validity.
- Submit Prompt: Submits the system prompt and initiates the AI's response generation.
- Submit Message: Submits the user's message and initiates the AI's response generation.
- Copy Output: Copies the contents of the output box to the clipboard.
- Clear Output: Clears the contents of the output box.

## Built with

- Python
- Tkinter
- OpenAI

## Note

This application requires a valid API key from OpenAI, which is used to interact with the OpenAI GPT-3.5 Turbo model for text generation. The performance of the application greatly depends on the provided API key.

## License

This project is open source and available under the MIT License.

## Disclaimer

This application is not an official product by OpenAI. It is developed for educational purposes and should not be used for malicious purposes.

## Contributing

Contributions, issues, and feature requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
