import PySimpleGUI as sg

Banana = 400

sg.theme('DarkGreen')
field = sg.Graph(
    canvas_size = (Banana,Banana),
    graph_bottom_left = (0,0),
    graph_top_right = (Banana,Banana),
    background_color= 'Black'
)

layout = [[field]]

window = sg.Window('snake', layout, return_keyboard_events = True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Left:37':
        print('left')

    if event == 'Right:39':
        print('right')

    if event == 'Up:38':
        print('top')

    if event == 'Down:40':
        print('down')

window.close()