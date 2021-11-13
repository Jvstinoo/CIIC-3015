def get_food():
    data = request.get_json()

    xPos = data['you']['head']['x']
    food = [list(i.values()) for i in list(data['board']['food'])]
    near = (n.abs([i[0]-xPos for i in food])).argmin()

    return food[near]


def snake_position():
    data = request.get_json()
    snakesX = list()
    snakesY = list()
    xPos = data['you']['head']['x']
    yPos = data['you']['head']['y']
    for i in data['board']['snakes'][1:]:
        for j in i['body']:
            snakesX.append(j.get('x'))
            snakesY.append(j.get('y'))

    if (xPos+1) in snakesX or (yPos+1) in snakesY:
        return False
    else:
        return True


def wall_collide():
    data = request.get_json()
    xPos = data['you']['head']['x']
    yPos = data['you']['head']['y']
    lengthX = data['board']['width']
    lengthY = data['board']['height']

    if xPos == lengthX-1 and yPos < lengthY:
        move = 'up'
    if yPos == lengthY-1 and xPos > 0:
        move = 'left'
    if xPos == 0 and yPos > 0:
        move = 'down'
    if yPos == 0 and xPos == 0:
        move = 'right'
    return move


@app.post("/move")
def handle_move():

    # Left off figuring out how to get all body positions to avoid colliding when snake length gets too big :D
    data = request.get_json()
    xPos = data['you']['head']['x']
    yPos = data['you']['head']['y']
    lengthX = data['board']['width']
    lengthY = data['board']['height']
    if (xPos == lengthX-1) or (xPos == 0) or (yPos == lengthY-1) or (yPos == 0):
        move = wall_collide

    moves = ['left', 'right', 'up', 'down']
    neck = data['you']['body'][1]

    if neck["x"] < xPos:  # my neck is left of my head
        moves.remove("left")
    elif neck["x"] > xPos:  # my neck is right of my head
        moves.remove("right")
    elif neck["y"] < yPos:  # my neck is below my head
        moves.remove("down")
    elif neck["y"] > yPos:  # my neck is above my head
        moves.remove("up")

    if get_food()[0] < xPos and 'left' in moves and snake_position():
        moves.remove('right')
        moves.remove('down')
        moves.remove('up')
    elif get_food()[0] > xPos and 'right' in moves and snake_position():
        moves.remove('left')
        moves.remove('down')
        moves.remove('up')
    elif get_food()[1] < yPos and 'down' in moves and snake_position():
        moves.remove('left')
        moves.remove('right')
        moves.remove('up')
    elif get_food()[1] > yPos and 'up' in moves and snake_position():
        moves.remove('right')
        moves.remove('left')
        moves.remove('down')

    move = random.choice(moves)
    return {"move": move}
