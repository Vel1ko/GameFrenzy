import PySimpleGUI as sg

def meny_window(DarkBlue14):
    sg.theme('DarkBlue14')
    sg.set_options(font = 'Franklin 15', button_element_size=(4,4))
    button_size = (4,4)
    layout = [
        [sg.Button('uno', size = button_size),sg.Button('Dos', size = button_size),sg.Button('tres', size = button_size)],
    ]

    window =  sg.Window('meny', layout)
    event, values = window.read()
    window.close()

meny_window('Darkblue14')