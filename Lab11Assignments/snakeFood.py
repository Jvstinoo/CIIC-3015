# First get food position and compare it to hazards/body parts and discard the ones occupied, finally compare the left ones with my position(head)
import numpy as n


def SnakeFood(dic):
    hazards = [tuple(i.values()) for i in list(dic['board']['hazards'])]

    second_body_parts = [tuple(i.values())
                         for i in list(dic['board']['snakes'][1]['body'])]

    food = [list(i.values()) for i in list(
        dic['board']['food']) if (tuple(i.values()) not in second_body_parts) and (tuple(i.values()) not in hazards)]

    head = [dic['you']['head']['x'], dic['you']['head']['y']]

    near = (n.abs([i[0]-head[0] for i in food])).argmin()

    return tuple(food[near])


print(SnakeFood({"game": {"id": "game-00fe20da-94ad-11ea-bb37", "ruleset": {"name": "standard", "version": "v.1.2.3"}, "timeout": 500}, "turn": 14,
                 "board": {"height": 11, "width": 11, "food": [{"x": 5, "y": 5}, {"x": 9, "y": 0}, {"x": 2, "y": 6}], "hazards": [{"x": 3, "y": 2}], "snakes": [{"id": "snake-508e96ac-94ad-11ea-bb37", "name": "My Snake", "health": 54, "body": [{"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0}], "latency": "111", "head": {"x": 0, "y": 0}, "length": 3,
                                                                                                                                                                 "shout": "why are we shouting??", "squad": ""}, {"id": "snake-b67f4906-94ae-11ea-bb37", "name": "Another Snake", "health": 16, "body": [{"x": 5, "y": 4}, {"x": 5, "y": 3}, {"x": 6, "y": 3}, {"x": 6, "y": 2}, {"x": 2, "y": 6}], "latency": "222", "head": {"x": 5, "y": 4}, "length": 4, "shout": "I'm not really sure...", "squad": ""}]}, "you": {"id": "snake-508e96ac-94ad-11ea-bb37",


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        "name": "My Snake", "health": 54, "body": [{"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0}], "latency": "111", "head": {"x": 0, "y": 0}, "length": 3, "shout": "why are we shouting??", "squad": ""}}))


print(SnakeFood({"game": {"id": "game-00fe20da-94ad-11ea-bb37", "ruleset": {"name": "standard", "version": "v.1.2.3"}, "timeout": 500}, "turn": 14, "board": {"height": 11, "width": 11, "food": [{"x": 5, "y": 5}, {"x": 9, "y": 0}], "hazards": [{"x": 3, "y": 2}], "snakes": [{"id": "snake-508e96ac-94ad-11ea-bb37", "name": "My Snake", "health": 54, "body": [{"x": 4, "y": 3}, {"x": 4, "y": 2}, {"x": 4, "y": 1}], "latency": "111", "head": {"x": 4, "y": 3}, "length": 3, "shout": "why are we shouting??", "squad": ""}, {
      "id": "snake-b67f4906-94ae-11ea-bb37", "name": "Another Snake", "health": 16, "body": [{"x": 5, "y": 4}, {"x": 5, "y": 3}, {"x": 6, "y": 3}, {"x": 6, "y": 2}], "latency": "222", "head": {"x": 5, "y": 4}, "length": 4, "shout": "I'm not really sure...", "squad": ""}]}, "you": {"id": "snake-508e96ac-94ad-11ea-bb37", "name": "My Snake", "health": 54, "body": [{"x": 4, "y": 3}, {"x": 4, "y": 2}, {"x": 4, "y": 1}], "latency": "111", "head": {"x": 4, "y": 3}, "length": 3, "shout": "why are we shouting??", "squad": ""}}))

print(SnakeFood({"game": {"id": "game-00fe20da-94ad-11ea-bb37", "ruleset": {"name": "standard", "version": "v.1.2.3"}, "timeout": 500}, "turn": 14, "board": {"height": 11, "width": 11, "food": [{"x": 5, "y": 5}, {"x": 9, "y": 0}, {"x": 2, "y": 6}], "hazards": [{"x": 3, "y": 2}], "snakes": [{"id": "snake-508e96ac-94ad-11ea-bb37", "name": "My Snake", "health": 54, "body": [{"x": 8, "y": 0}, {"x": 7, "y": 0}, {"x": 6, "y": 0}], "latency": "111", "head": {"x": 8, "y": 0}, "length": 3, "shout": "why are we shouting??", "squad": ""}, {
      "id": "snake-b67f4906-94ae-11ea-bb37", "name": "Another Snake", "health": 16, "body": [{"x": 5, "y": 4}, {"x": 5, "y": 3}, {"x": 6, "y": 3}, {"x": 6, "y": 2}], "latency": "222", "head": {"x": 5, "y": 4}, "length": 4, "shout": "I'm not really sure...", "squad": ""}]}, "you": {"id": "snake-508e96ac-94ad-11ea-bb37", "name": "My Snake", "health": 54, "body": [{"x": 8, "y": 0}, {"x": 7, "y": 0}, {"x": 6, "y": 0}], "latency": "111", "head": {"x": 8, "y": 0}, "length": 3, "shout": "why are we shouting??", "squad": ""}}))
