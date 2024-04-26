
def ssp():

    import PySimpleGUI as sg
    import random

    sg.theme('DarkGrey13')
    layout = [ 
        [sg.Text('Sten Sax Påse', font = 'Franklin 30', justification= 'center')],
        [sg.Image(r'C:\Users\veljko.jovic\Desktop\Python Uppgifter\GameFrenzy\ROCK_PIC.png', size = (150, 200)),sg.Image(r'C:\Users\veljko.jovic\Desktop\Python Uppgifter\GameFrenzy\paper1.png', size = (150, 200), subsample= 3),sg.Image(r'C:\Users\veljko.jovic\Desktop\Python Uppgifter\GameFrenzy\scissors.png', size = (150, 200))],
        [sg.Button('Rock'), sg.Push(), sg.Push(), sg.Push(), sg.Button('Paper'), sg.Push(), sg.Push(), sg.Push(), sg.Button('Scissors')],
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