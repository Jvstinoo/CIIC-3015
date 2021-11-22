import logging
import os
import numpy as n
import random

from flask import Flask
from flask import request

import server_logic


app = Flask(__name__)


@app.get("/")
def handle_info():
    """
    This function is called when you register your Battlesnake on play.battlesnake.com
    See https://docs.battlesnake.com/guides/getting-started#step-4-register-your-battlesnake

    It controls your Battlesnake appearance and author permissions.
    For customization options, see https://docs.battlesnake.com/references/personalization

    TIP: If you open your Battlesnake URL in browser you should see this data.
    """
    print("INFO")
    return {
        "apiversion": "1",
        "author": "",
        "color": "#341d4a",
        "head": "sand-worm",
        "tail": "replit-notmark",
    }


@app.post("/start")
def handle_start():
    """
    This function is called everytime your snake is entered into a game.
    request.json contains information about the game that's about to be played.
    """
    data = request.get_json()

    print(f"{data['game']['id']} START")
    return "ok"


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


def get_food():
    data = request.get_json()

    xPos = data['you']['head']['x']
    food = [list(i.values()) for i in list(data['board']['food'])]
    near = (n.abs([i[0]-xPos for i in food])).argmin()

    return food[near]


def check_collision():
    data = request.get_json()

    xPos = data['you']['head']['x']
    yPos = data['you']['head']['y']
    lengthX = data['board']['width']
    lengthY = data['board']['height']
    if (xPos == 0) or (xPos == lengthX-1) or (yPos == 0) or (yPos == lengthY-1):
        return False
    else:
        return True


def snake_position():
    global move
    data = request.get_json()
    snakesX = list()
    snakesY = list()
    xPos = data['you']['head']['x']
    yPos = data['you']['head']['y']
    for i in data['board']['snakes']:
        for j in i['body']:
            snakesX.append(j.get('x'))
            snakesY.append(j.get('y'))
    if move == 'left':
        if (xPos-1 in snakesX) and (yPos-1 in snakesY):
            return False
        else:
            return True
    if move == 'right':
        if (xPos+1) in snakesX and (yPos+1) in snakesY:
            return False
        else:
            return True


def check_head():
    data = request.get_json()
    xPos = data['you']['head']['x']
    yPos = data['you']['head']['y']

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
    return moves


def possible_moves():
    data = request.get_json()
    global move
    xPos = data['you']['head']['x']
    yPos = data['you']['head']['y']
    my_bodyX = [i.get('x') for i in data['you']['body']]
    my_bodyY = [i.get('y') for i in data['you']['body']]

    moves = ['left', 'right', 'up', 'down']
    neck = data['you']['body'][1]

    if (move == 'left'):
        if (xPos-1 in my_bodyX):
            moves.remove('left')
    if (move == 'right'):
        if (xPos+1 in my_bodyX):
            moves.remove('right')
    if (move == 'up'):
        if (yPos+1 in my_bodyY):
            moves.remove('up')
    if (move == 'down'):
        if (yPos-1 in my_bodyY):
            moves.remove('down')

    if neck["x"] < xPos and ('left' in moves):  # my neck is left of my head
        moves.remove("left")
    if neck["x"] > xPos and ('right' in moves):  # my neck is right of my head
        moves.remove("right")
    if neck["y"] < yPos and ('down' in moves):  # my neck is below my head
        moves.remove("down")
    if neck["y"] > yPos and ('up' in moves):  # my neck is above my head
        moves.remove("up")

    return random.choice(moves)


def Survive():
    data = request.get_json()

    xPos = data['you']['head']['x']
    yPos = data['you']['head']['y']
    lengthX = data['board']['width']
    lengthY = data['board']['height']

    if (check_collision()) and (snake_position()) and ('left' in check_head()):
        move = 'left'
    elif (check_collision()) and (snake_position()) and ('right' in check_head()):
        move = 'right'
    elif (check_collision()) and (snake_position()) and ('down' in check_head()):
        move = 'down'
    elif (check_collision()) and (snake_position()) and ('up' in check_head()):
        move = 'up'
    elif not (check_collision()):
        # Maybe put the wall_collide function code in here since it is not working fast enough
        if(xPos == lengthX-1) and (yPos < lengthY) and snake_position():
            move = 'up'
        if (yPos == lengthY-1) and (xPos > 0) and snake_position():
            move = 'left'
        if (xPos == 0) and (yPos > 0) and snake_position():
            move = 'down'
        if (yPos == 0) and (xPos == 0) and snake_position():
            move = 'right'
        if (xPos < lengthX-1) and (yPos == 0) and (snake_position()):
            move = 'right'

    return move


def Eat_Food():
    data = request.get_json()

    xPos = data['you']['head']['x']
    yPos = data['you']['head']['y']
    lengthX = data['board']['width']
    lengthY = data['board']['height']

    if get_food()[0] < xPos and (check_collision) and (snake_position) and ('left' in check_head()):
        move = 'left'
    elif get_food()[0] > xPos and (check_collision) and (snake_position) and ('right' in check_head()):
        move = 'right'
    elif get_food()[1] < yPos and (check_collision) and (snake_position) and ('down' in check_head()):
        move = 'down'
    elif get_food()[1] > yPos and (check_collision) and (snake_position) and ('up' in check_head()):
        move = 'up'
    elif (xPos == lengthX-1) or (xPos == 0) or (yPos == lengthY-1) or (yPos == 0):
        # Maybe put the wall_collide function code in here since it is not working fast enough
        if xPos == lengthX-1 and yPos < lengthY:
            move = 'up'
        if yPos == lengthY-1 and xPos > 0:
            move = 'left'
        if xPos == 0 and yPos > 0:
            move = 'down'
        if yPos == 0 and xPos == 0:
            move = 'right'
        if (xPos < lengthX-1) and (yPos == 0) and (snake_position()):
            move = 'right'
    else:
        # Create list in another function with the possible moves to make depending on snake bodies.
        move = possible_moves()

    return move


@app.post("/move")
def handle_move():
    data = request.get_json()
    '''try: 
      [list(i.values()) for i in list(data['board']['food'])]
    except:
      move = Survive()
      
    else:
      move = Eat_Food()'''
    move = Eat_Food()

    print(f'MOVE {move}', data)
    return {"move": move}


@app.post("/end")
def end():
    """
    This function is called when a game your snake was in ends.
    It's purely for informational purposes, you don't have to make any decisions here.
    """
    data = request.get_json()

    print(f"{data['game']['id']} END")
    return "ok"


if __name__ == "__main__":
    logging.getLogger("werkzeug").setLevel(logging.ERROR)

    print("Starting Battlesnake Server...")
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port, debug=True)
