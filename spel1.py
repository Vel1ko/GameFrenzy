
def ssp():
    import PySimpleGUI as sg
    import random
    layout = [ 
        [sg.Text('Sten ,Sax, påse')],
        [sg.Button('Rock'), sg.Button('Paper'), sg.Button('Scissors')],
        [sg.Text(size=(20,1), key='-RESULT-')],
        [sg.Button('Avsluta')]
    ]

    window = sg.Window('Sten Sax Påse').Layout(layout)

    while True:
        event, values = window.Read()

        if event in (None, 'Avsluta'):
            break
        elif event in ('Rock', 'Paper', 'Scissors'):
            user_choice = event.lower()
            computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
            winner = (user_choice, computer_choice)
            window['-RESULT-'].update(winner)

ssp()