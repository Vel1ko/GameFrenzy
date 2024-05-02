def snake_game():
    import PySimpleGUI as sg
    from time import time
    from random import randint

    def convert_pos_to_pixel(cell):
        tl = cell[0] * CELL_SIZE, cell[1] * CELL_SIZE
        br = tl[0] + CELL_SIZE, tl[1] + CELL_SIZE
        return tl, br

    def place_munch():
        munch_pos = randint(0, CELL_NUM -1), randint(0, CELL_NUM -1)
        while munch_pos in snake_body:
            munch_pos = randint(0, CELL_NUM -1), randint(0, CELL_NUM -1)
        return munch_pos
    #konstanterna
    FIELD_SIZE = 400
    CELL_NUM = 10
    CELL_SIZE = FIELD_SIZE / CELL_NUM


    #Snake
    snake_body = [(4,4),(3,4),(2,4)]
    DIRECTIONS = {'left': (-1,0),'right': (1,0), 'up' :(0,1), 'down':(0,-1)}
    direction = DIRECTIONS ['up']

    #Frukt
    munch_pos = place_munch()
    munch_eaten = False

    sg.theme('DarkBlue')
    field = sg.Graph(
        canvas_size = (FIELD_SIZE,FIELD_SIZE),
        graph_bottom_left = (0,0),
        graph_top_right = (FIELD_SIZE,FIELD_SIZE),
        background_color= 'PaleGreen1'
    )

    layout = [[field]]

    window = sg.Window('snake', layout, return_keyboard_events = True)

    start_time = time()

    while True:
        event, values = window.read(timeout = 10)
        if event == sg.WIN_CLOSED:
            break

        if event == 'Left:37':
            direction = DIRECTIONS ['left']

        if event == 'Right:39':
            direction = DIRECTIONS ['right']

        if event == 'Up:38':
            direction = DIRECTIONS ['up']

        if event == 'Down:40':
            direction = DIRECTIONS ['down']
        
        time_since_start = time() - start_time
        if time_since_start >= 0.2:
            start_time = time()

            #munch snake collision
            if snake_body[0] == munch_pos:
                munch_pos = place_munch()
                munch_eaten = True
                

            #Snake update
            new_head = (snake_body[0][0] + direction[0],snake_body[0][1] + direction[1])
            snake_body.insert(0,new_head)
            if not munch_eaten:
                snake_body.pop()
            else:
              munch_eaten = False
            
            #Collison death
            if not 0 <= snake_body[0][0] <= CELL_NUM -1 or \
            not 0 <= snake_body[0][1] <= CELL_NUM -1:
                break
        
            field.DrawRectangle((0,0),(FIELD_SIZE,FIELD_SIZE), 'PaleGreen1')

            tl, br = convert_pos_to_pixel(munch_pos)
            field.DrawRectangle(tl,br,'red')

            #Snake drawn
            for index, part in enumerate(snake_body):
                tl, br = convert_pos_to_pixel(part)
                color = 'Springgreen4' if index == 0 else 'limeGreen'
                field.DrawRectangle(tl,br,color)

    window.close()