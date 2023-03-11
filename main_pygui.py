import PySimpleGUI as sg
import openai

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

# Define the PySimpleGUI layout
sg.theme('DarkGrey1')
layout = [[sg.Text('ChatGPT Client v1', font=('Helvetica', 20), pad=(5, 5))],
          [sg.Multiline('', key='conversation', font=('Helvetica', 14), size=(60, 10), pad=(5, 5))],
          [sg.Input('', key='input_message', font=('Helvetica', 14), size=(50, 1), pad=(5, 5)),
           sg.Button('Send', font=('Helvetica', 14), pad=(5, 5))]]

# Create the PySimpleGUI window
window = sg.Window('ChatGPT Client by LopeKinz', layout)

# Start the PySimpleGUI event loop
while True:
    event, values = window.read()

    # Exit the event loop when the window is closed
    if event == sg.WINDOW_CLOSED:
        break


    # Send the user's message and get a response from ChatGPT
    if event == 'Send':
        # Get the user's input message
        message = values['input_message']

        # Clear the input field
        window['input_message'].update('')

        # Add the user's message to the conversation area
        window['conversation'].print('You: ' + message + '\n\n')

        # Call ChatGPT to get a response
        response = chat_gpt(message)

        # Add the response to the conversation area
        window['conversation'].print('ChatGPT: ' + response + '\n') 

# Close the PySimpleGUI window when the event loop is exited
window.close()
