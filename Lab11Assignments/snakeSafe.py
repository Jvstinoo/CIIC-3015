def SnakeSafe(dic, x, y):
    snake_parts = tuple()
    hazards = dic['board']['hazards'][0]['x'], dic['board']['hazards'][0]['y']
    for i in dic['board']['snakes']:
        snake_parts += (i['body'][0]['x'], i['body'][0]['y']), (i['body'][1]
                                                                ['x'], i['body'][1]['y']), (i['body'][2]['x'], i['body'][2]['y'])
    x_snake = [i[0] for i in list(snake_parts)]
    y_snake = [i[1] for i in list(snake_parts)]
    return not ((x in x_snake or x == hazards[0]) or (y in y_snake or y == hazards[1]))


print(SnakeSafe({"game": {"id": "game-00fe20da-94ad-11ea-bb37", "ruleset": {"name": "standard", "version": "v.1.2.3"}, "timeout": 500}, "turn": 14, "board": {"height": 11, "width": 11, "food": [{"x": 5, "y": 5}, {"x": 9, "y": 0}, {"x": 2, "y": 6}], "hazards": [{"x": 3, "y": 2}], "snakes": [{"id": "snake-508e96ac-94ad-11ea-bb37", "name": "My Snake", "health": 54, "body": [{"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0}], "latency": "111", "head": {"x": 0, "y": 0}, "length": 3, "shout": "why are we shouting??", "squad": ""}, {
      "id": "snake-b67f4906-94ae-11ea-bb37", "name": "Another Snake", "health": 16, "body": [{"x": 5, "y": 4}, {"x": 5, "y": 3}, {"x": 6, "y": 3}, {"x": 6, "y": 2}], "latency": "222", "head": {"x": 5, "y": 4}, "length": 4, "shout": "I'm not really sure...", "squad": ""}]}, "you": {"id": "snake-508e96ac-94ad-11ea-bb37", "name": "My Snake", "health": 54, "body": [{"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0}], "latency": "111", "head": {"x": 0, "y": 0}, "length": 3, "shout": "why are we shouting??", "squad": ""}}, 2, 0))
print(SnakeSafe({"game": {"id": "game-00fe20da-94ad-11ea-bb37", "ruleset": {"name": "standard", "version": "v.1.2.3"}, "timeout": 500}, "turn": 14, "board": {"height": 11, "width": 11, "food": [{"x": 5, "y": 5}, {"x": 9, "y": 0}, {"x": 2, "y": 6}], "hazards": [{"x": 3, "y": 2}], "snakes": [{"id": "snake-508e96ac-94ad-11ea-bb37", "name": "My Snake", "health": 54, "body": [{"x": 4, "y": 3}, {"x": 4, "y": 2}, {"x": 4, "y": 1}], "latency": "111", "head": {"x": 4, "y": 3}, "length": 3, "shout": "why are we shouting??", "squad": ""}, {
      "id": "snake-b67f4906-94ae-11ea-bb37", "name": "Another Snake", "health": 16, "body": [{"x": 5, "y": 4}, {"x": 5, "y": 3}, {"x": 6, "y": 3}, {"x": 6, "y": 2}], "latency": "222", "head": {"x": 5, "y": 4}, "length": 4, "shout": "I'm not really sure...", "squad": ""}]}, "you": {"id": "snake-508e96ac-94ad-11ea-bb37", "name": "My Snake", "health": 54, "body": [{"x": 4, "y": 3}, {"x": 4, "y": 2}, {"x": 4, "y": 1}], "latency": "111", "head": {"x": 4, "y": 3}, "length": 3, "shout": "why are we shouting??", "squad": ""}}, 8, 8))
