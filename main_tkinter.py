import tkinter as tk
from tkinter import scrolledtext
import openai
import threading

# Set up OpenAI API credentials
openai.api_key = "YOUR_TOKEN"

# Define the ChatGPT function that sends a prompt to OpenAI and returns the response
def chat_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text
    return message.strip()

# Define the GUI class
class ChatGUI:
    def __init__(self, master):
        self.master = master
        master.title("ChatGPT GUI")

        # Create the text area where the conversation will be displayed
        self.conversation = scrolledtext.ScrolledText(master, height=20, width=50)
        self.conversation.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        # Create the text input field
        self.input_field = tk.Entry(master, width=40)
        self.input_field.grid(row=1, column=0, padx=5, pady=5)

        # Create the send button
        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=5, pady=5)



    # Method to send a message and get a response from ChatGPT
    def send_message(self):
        # Get the user's input message
        message = self.input_field.get()

        # Clear the input field
        self.input_field.delete(0, tk.END)

        # Add the user's message to the conversation area
        self.conversation.insert(tk.END, "You: " + message + "\n")

        # Call ChatGPT to get a response
        threading.Thread(target=self.get_response, args=(message,)).start()

    # Method to get a response from ChatGPT and add it to the conversation area
    def get_response(self, message):
        response = chat_gpt(message)

        # Add the response to the conversation area
        self.conversation.insert(tk.END, "ChatGPT: " + response + "\n")

    # Method to toggle the GUI theme between light and dark mode


root = tk.Tk()
chat_gui = ChatGUI(root)
root.mainloop()
