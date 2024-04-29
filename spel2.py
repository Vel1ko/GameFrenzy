import PySimpleGUI as sg

FIELD_SIZE = 400
CELL_NUM = 10
CELL_SIZE = FIELD_SIZE / CELL_NUM


munch = (2,4)

sg.theme('DarkGreen')
field = sg.Graph(
    canvas_size = (FIELD_SIZE,FIELD_SIZE),
    graph_bottom_left = (0,0),
    graph_top_right = (FIELD_SIZE,FIELD_SIZE),
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