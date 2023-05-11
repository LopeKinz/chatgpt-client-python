import PySimpleGUI as sg
import openai
import pyperclip

# Set up OpenAI API credentials
openai.api_key = "YOUR_API_KEY"

# Define the ChatGPT function that sends a prompt to OpenAI and returns the response
def chat_gpt(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text
    return message.strip()

# Define the PySimpleGUI layout
sg.theme('LightGrey1')
layout = [
    [sg.Text('ChatGPT', font=('Helvetica', 20), pad=(5, 5))],
    [sg.Multiline('', key='conversation', font=('Helvetica', 14), size=(60, 10), pad=(5, 5))],
    [
        sg.Input('', key='input_message', font=('Helvetica', 14), size=(50, 1), pad=(5, 5)),
        sg.Button('Send', font=('Helvetica', 14), pad=(5, 5))
    ],
    [sg.Button('Toggle Theme', font=('Helvetica', 14), pad=(5, 5))],
    [
        sg.TabGroup([
            [
                sg.Tab('Jailbreaking', [
                    [sg.Button('Button 1'), sg.Button('Button 2'), sg.Button('Button 3'), sg.Button('Button 4'), sg.Button('Button 5')]
                ])
            ]
        ])
    ]
]

# Create the PySimpleGUI window
window = sg.Window('ChatGPT', layout)

# Start the PySimpleGUI event loop
while True:
    event, values = window.read()

    # Exit the event loop when the window is closed
    if event == sg.WINDOW_CLOSED:
        break

    # Toggle between light and dark theme
    if event == 'Toggle Theme':
        if sg.theme() == 'LightGrey1':
            sg.theme('DarkGrey1')
        else:
            sg.theme('LightGrey1')

    # Send the user's message and get a response from ChatGPT
    if event == 'Send':
        # Get the user's input message
        message = values['input_message']

        # Clear the input field
        window['input_message'].update('')

        # Add the user's message to the conversation area
        window['conversation'].print(f'You: {message}')

        # Call ChatGPT to get a response
        response = chat_gpt(message)

        # Add the response to the conversation area
        window['conversation'].print(f'ChatGPT: {response}')

    # Copy the text to the clipboard when the button is clicked
    if event.startswith('Button'):
        pyperclip.copy(f'Button {event[-1]} text copied to clipboard!')

# Close the PySimpleGUI window when the event loop is exited
window.close()
