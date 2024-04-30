import PySimpleGUI as sg
from spel1 import ssp
from spel2 import snake_game

def create_window(theme):
    sg.theme(theme)
    sg.set_options(font = 'Franklin 15', button_element_size=(4,4))
    button_size = (8,6)
    layout = [
        [sg.Text('GameFrenzy', font = 'Franklin 30', justification = 'center', right_click_menu= theme_menu)],
        [sg.Button('Sten sax påse', size = button_size),sg.Button('Snake', size = button_size),sg.Button('Spel 3', size = button_size)],
    ]

    return sg.Window('meny', layout)

theme_menu = ['menu',['DarkBlue14', 'DarkGrey6', 'DarkRed', 'PythonPlus', 'Random']]
window = create_window('')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'DarkBlue14' or event == 'DarkGrey6' or event == 'DarkRed' or event == 'PythonPlus' or event == 'Random':
        window.close()
        window = create_window(event)

    if event == 'Sten sax påse':
        ssp()
    
    if event == 'Snake':
        snake_game()

window.close()