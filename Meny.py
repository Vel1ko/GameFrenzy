import PySimpleGUI as sg

def meny_window(theme):
    sg.theme(theme)
    sg.set_options(font = 'Franklin 15', button_element_size=(4,4))
    button_size = (8,6)
    layout = [
        [sg.Text('GameFrenzy', font = 'Franklin 30', justification = 'center', right_click_menu= theme_menu)],
        [sg.Button('Spel 1', size = button_size),sg.Button('Spel 2', size = button_size),sg.Button('Spel 3', size = button_size)],
    ]

    return sg.Window('meny', layout)

theme_menu = ['menu',['DarkBlue14', 'DarkGrey6', 'DarkRed']]
window = meny_window('DarkRed')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()