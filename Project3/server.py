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


def get_food():
    data = request.get_json()

    xPos = data['you']['head']['x']
    food = [list(i.values()) for i in list(data['board']['food'])]
    near = (n.abs([i[0]-xPos for i in food])).argmin()

    return food[near]


def snake_position():
    data = request.get_json()
    xPos = data['you']['head']['x']
    yPos = data['you']['head']['y']
    snakesX = list()
    snakesY = list()
    for i in data['board']['snakes']:
        for j in i['body']:
            snakesX.append(j.get('x'))
            snakesY.append(j.get('y'))
    if (xPos+1 in snakesX) and (yPos+1 in snakesY):
        return False
    else:
        return True


def wall_collide():
    move = 'right'
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

    moves = ['left', 'right', 'up', 'down']

    neck = data['you']['body'][1]
    xPos = data['you']['head']['x']
    yPos = data['you']['head']['y']
    lengthX = data['board']['width']
    lengthY = data['board']['height']

    if neck["x"] < xPos:  # my neck is left of my head
        moves.remove("left")
    elif neck["x"] > xPos:  # my neck is right of my head
        moves.remove("right")
    elif neck["y"] < yPos:  # my neck is below my head
        moves.remove("down")
    elif neck["y"] > yPos:  # my neck is above my head
        moves.remove("up")

    '''if get_food()[0] < xPos and 'left' in moves and snake_position():
      move = 'left'
    elif get_food()[0] > xPos and 'right' in moves and snake_position():
      move = 'right'
    elif get_food()[1] < yPos and 'down' in moves and snake_position():
      move = 'down'
    elif get_food()[1] > yPos and 'up' in moves and snake_position():
      move = 'up' '''

    wall_collide()
    move = random.choice(moves)

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
