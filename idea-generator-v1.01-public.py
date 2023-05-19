import tkinter as tk
import tkinter.scrolledtext as scrolledtext
from tkinter import messagebox, ttk
import pyperclip
import openai
import threading
import time

# Initial setup for OpenAI API key
openai.api_key = ''  # replace with your actual key


# Define IdeaGenerator class to handle interactions with OpenAI and the user interface
class IdeaGenerator:
    def __init__(self, root):
        self.is_running = True
        self.messages = []
        self.valid_key = False
        root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.durations = []
        self.root = root
        root.title("OpenAI ChatGPT 3.5 Turbo")

        # GUI Components
        self.create_gui_elements(root)
        self.configure_grid(root)

    def create_gui_elements(self, root):
        # API Key Entry Section
        self.create_api_key_section(root)
        # Prompt Entry Section
        self.create_prompt_section(root)
        # Message Entry Section
        self.create_message_section(root)
        # Output and Controls Section
        self.create_output_and_controls_section(root)

    def create_api_key_section(self, root):
        """Creates components for API Key entry"""
        self.api_key_label = tk.Label(root, text="API Key:")
        self.api_key_label.grid(row=0, column=0, sticky='w', columnspan=4)
        self.api_key_entry = tk.Entry(root)
        self.api_key_entry.grid(row=1, column=0, columnspan=3, sticky='ew')
        self.submit_key_button = tk.Button(root, text="Submit Key", command=self.submit_key)
        self.submit_key_button.grid(row=1, column=3, sticky='ew')

    def create_prompt_section(self, root):
        """Creates components for Prompt entry"""
        self.prompt_content = tk.StringVar()
        self.prompt_label = tk.Label(root, text="Prompt:")
        self.prompt_label.grid(row=2, column=0, sticky='w', columnspan=4)
        self.prompt_entry = tk.Text(root, height=4, width=50)
        self.prompt_entry.grid(row=3, column=0, columnspan=4, sticky='nsew')

    def create_message_section(self, root):
        """Creates components for Message entry"""
        self.message_label = tk.Label(root, text="Message:")
        self.message_label.grid(row=4, column=0, sticky='w', columnspan=4)
        self.message_entry = tk.Text(root, height=7, width=50)
        self.message_entry.grid(row=5, column=0, columnspan=4, sticky='nsew')

    def create_output_and_controls_section(self, root):
        """Creates components for Output box and Control buttons"""
        self.is_generating = False
        self.estimated_duration = 5
        self.idea_box = scrolledtext.ScrolledText(root, wrap=tk.WORD)
        self.idea_box.grid(row=7, column=0, columnspan=4, sticky='nsew')
        self.progress = ttk.Progressbar(root, mode='determinate', maximum=self.estimated_duration*100)
        self.progress.grid(row=8, column=0, columnspan=4, sticky='ew')
        self.progress.grid_remove()

        # Control Buttons
        self.create_control_buttons(root)

    def create_control_buttons(self, root):
        """Creates control buttons"""
        self.generate_button = tk.Button(root, text="Submit Prompt", command=self.start_generate_thread)
        self.generate_button.grid(row=6, column=0, sticky='ew')
        self.message_button = tk.Button(root, text="Submit Message", command=self.start_message_thread)
        self.message_button.grid(row=6, column=1, sticky='ew')
        self.copy_button = tk.Button(root, text="Copy Output", command=self.copy_idea)
        self.copy_button.grid(row=6, column=2, sticky='ew')
        self.clear_button = tk.Button(root, text="Clear Output", command=self.clear_idea)
        self.clear_button.grid(row=6, column=3, sticky='ew')

    def configure_grid(self, root):
        """Configures grid for the root window"""
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        root.grid_columnconfigure(2, weight=1)
        root.grid_columnconfigure(3, weight=1)

        # Adjust row configurations as needed
        root.grid_rowconfigure(0, weight=0, pad=5)  # api_key_label
        root.grid_rowconfigure(1, weight=0, pad=5)  # api_key_entry and submit_key_button
        root.grid_rowconfigure(2, weight=0, pad=5)  # prompt_label
        root.grid_rowconfigure(3, weight=1, pad=5)  # prompt_entry
        root.grid_rowconfigure(4, weight=0, pad=5)  # message_label
        root.grid_rowconfigure(5, weight=1, pad=5)  # message_entry
        root.grid_rowconfigure(6, weight=0, pad=5)  # buttons row
        root.grid_rowconfigure(7, weight=10, pad=0)  # idea_box gets more space
        root.grid_rowconfigure(8, weight=0, pad=0)  # progress bar
        root.grid_rowconfigure(9, weight=0, pad=0)  # empty row for potential future use

    def generate_idea(self):
        self.is_generating = True
        self.progress.grid()
        self.progress['value'] = 0
        start_time = time.time()

        prompt_content = self.prompt_entry.get("1.0",'end-1c')
        self.messages.append({'role': 'system', 'content': prompt_content})   # Use 'system' role for prompt

        retries = 0
        while retries < 3 and self.is_running:
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=self.messages,
                )
                break
            except openai.error.RateLimitError:
                retries += 1
                time.sleep(1)
            except openai.error.AuthenticationError:
                self.idea_box.insert('1.0', "\n----------------\n")  
                self.idea_box.insert('1.0', "Invalid OpenAI API key!")
                return

        if self.is_running:
            self.messages.append(response['choices'][0]['message'])
            self.idea_box.insert('1.0', "\n----------------\n")  
            self.idea_box.insert('1.0', response['choices'][0]['message']['content'].strip())
            end_time = time.time()
            self.durations.append(end_time - start_time)
            self.estimated_duration = sum(self.durations) / len(self.durations)
            self.progress['maximum'] = self.estimated_duration*100
            self.progress.stop()
            self.progress.grid_remove()
            self.is_generating = False

    def generate_message(self):
        self.is_generating = True
        self.progress.grid()
        self.progress['value'] = 0
        start_time = time.time()

        message_content = self.message_entry.get("1.0",'end-1c')
        self.messages.append({'role': 'user', 'content': message_content})    # Use 'user' role for message

        retries = 0
        while retries < 3 and self.is_running:
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=self.messages,
                )
                break
            except openai.error.RateLimitError:
                retries += 1
                time.sleep(1)
            except openai.error.AuthenticationError:
                self.idea_box.insert('1.0', "\n----------------\n")  
                self.idea_box.insert('1.0', "Invalid OpenAI API key!")
                return

        if self.is_running:
            self.messages.append(response['choices'][0]['message'])
            self.idea_box.insert('1.0', "\n----------------\n")  
            self.idea_box.insert('1.0', response['choices'][0]['message']['content'].strip())
            self.message_entry.delete('1.0', tk.END)
            end_time = time.time()
            self.durations.append(end_time - start_time)
            self.estimated_duration = sum(self.durations) / len(self.durations)
            self.progress['maximum'] = self.estimated_duration*100
            self.progress.stop()
            self.progress.grid_remove()
            self.is_generating = False

    def start_generate_thread(self):
        if not self.is_generating and self.valid_key:
            self.messages = []
            threading.Thread(target=self.generate_idea).start()
            threading.Thread(target=self.run_progress).start()
        else:
            if not self.valid_key:
                messagebox.showinfo("API Key Required!", "Please submit a valid API Key.")


    def start_message_thread(self):
        if not self.is_generating and self.valid_key and self.messages:
            threading.Thread(target=self.generate_message).start()
            threading.Thread(target=self.run_progress).start()
        else:
            if not self.valid_key:
                messagebox.showinfo("API Key Required!", "Please submit a valid API Key.")


    def copy_idea(self):
        pyperclip.copy(self.idea_box.get('1.0', tk.END))
        messagebox.showinfo("Copied!", "Output has been copied to clipboard")

    def clear_idea(self):
        self.idea_box.delete('1.0', tk.END)

    def run_progress(self):
        while self.is_generating:
            if self.progress['value'] < self.progress['maximum']:
                self.progress['value'] += 1
            else:
                self.progress['value'] = 0
            time.sleep(0.01)

    def on_closing(self):
        self.is_running = False
        self.root.destroy()

    def submit_key(self):
        # Try to make a test API call to verify if the key is valid.
        test_key = self.api_key_entry.get().strip()
        if test_key:
            openai.api_key = test_key
            try:
                openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "system", "content": "You are a helpful assistant."}],
                    max_tokens=5,
                )
                self.valid_key = True
                self.api_key_entry.delete(0, 'end')  # New line to clear the API key entry box
                messagebox.showinfo("API Key Updated!", "The API Key has been updated successfully")
            except openai.error.OpenAIError as error:
                self.valid_key = False
                messagebox.showinfo("API Key Invalid!", "The entered API Key is invalid. Please enter a valid key.")
        else:
            messagebox.showinfo("API Key Required!", "Please enter an API Key.")

# Create the main window and start the Tkinter event loop
root = tk.Tk()
root.geometry("600x400")  
root.minsize(600, 600)
gui = IdeaGenerator(root)
root.mainloop()

