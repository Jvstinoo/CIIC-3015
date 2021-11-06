def SnakeNeck(dic):
    # Get both x and y head positions
    head = dic['you']['head']['x'], dic['you']['head']['y']
    # Get both x and y neck positions
    neck = dic['you']['body'][1]['x'], dic['you']['body'][1]['y']

    if head[0] == neck[0]:
        if head[1] < neck[1]:
            return 'up'
        return 'down'
    if head[1] == neck[1]:
        if head[0] < neck[0]:
            return 'right'
        return 'left'


print(SnakeNeck({"game": {"id": "game-00fe20da-94ad-11ea-bb37", "ruleset": {"name": "standard", "version": "v.1.2.3"}, "timeout": 500}, "turn": 14, "board": {"height": 11, "width": 11, "food": [{"x": 5, "y": 5}, {"x": 9, "y": 0}, {"x": 2, "y": 6}], "hazards": [{"x": 3, "y": 2}], "snakes": [{"id": "snake-508e96ac-94ad-11ea-bb37", "name": "My Snake", "health": 54, "body": [{"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0}], "latency": "111", "head": {"x": 0, "y": 0}, "length": 3, "shout": "why are we shouting??", "squad": ""}, {
      "id": "snake-b67f4906-94ae-11ea-bb37", "name": "Another Snake", "health": 16, "body": [{"x": 5, "y": 4}, {"x": 5, "y": 3}, {"x": 6, "y": 3}, {"x": 6, "y": 2}], "latency": "222", "head": {"x": 5, "y": 4}, "length": 4, "shout": "I'm not really sure...", "squad": ""}]}, "you": {"id": "snake-508e96ac-94ad-11ea-bb37", "name": "My Snake", "health": 54, "body": [{"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0}], "latency": "111", "head": {"x": 0, "y": 0}, "length": 3, "shout": "why are we shouting??", "squad": ""}}))
print(SnakeNeck({"game": {"id": "game-00fe20da-94ad-11ea-bb37", "ruleset": {"name": "standard", "version": "v.1.2.3"}, "timeout": 500}, "turn": 14, "board": {"height": 11, "width": 11, "food": [{"x": 5, "y": 5}, {"x": 9, "y": 0}, {"x": 2, "y": 6}], "hazards": [{"x": 3, "y": 2}], "snakes": [{"id": "snake-508e96ac-94ad-11ea-bb37", "name": "My Snake", "health": 54, "body": [{"x": 8, "y": 0}, {"x": 7, "y": 0}, {"x": 6, "y": 0}], "latency": "111", "head": {"x": 8, "y": 0}, "length": 3, "shout": "why are we shouting??", "squad": ""}, {
      "id": "snake-b67f4906-94ae-11ea-bb37", "name": "Another Snake", "health": 16, "body": [{"x": 5, "y": 4}, {"x": 5, "y": 3}, {"x": 6, "y": 3}, {"x": 6, "y": 2}], "latency": "222", "head": {"x": 5, "y": 4}, "length": 4, "shout": "I'm not really sure...", "squad": ""}]}, "you": {"id": "snake-508e96ac-94ad-11ea-bb37", "name": "My Snake", "health": 54, "body": [{"x": 8, "y": 0}, {"x": 7, "y": 0}, {"x": 6, "y": 0}], "latency": "111", "head": {"x": 8, "y": 0}, "length": 3, "shout": "why are we shouting??", "squad": ""}}))
print(SnakeNeck({"game": {"id": "game-00fe20da-94ad-11ea-bb37", "ruleset": {"name": "standard", "version": "v.1.2.3"}, "timeout": 500}, "turn": 14, "board": {"height": 11, "width": 11, "food": [{"x": 5, "y": 5}, {"x": 9, "y": 0}, {"x": 2, "y": 6}], "hazards": [{"x": 3, "y": 2}], "snakes": [{"id": "snake-508e96ac-94ad-11ea-bb37", "name": "My Snake", "health": 54, "body": [{"x": 4, "y": 1}, {"x": 4, "y": 2}, {"x": 4, "y": 3}], "latency": "111", "head": {"x": 4, "y": 1}, "length": 3, "shout": "why are we shouting??", "squad": ""}, {
      "id": "snake-b67f4906-94ae-11ea-bb37", "name": "Another Snake", "health": 16, "body": [{"x": 5, "y": 4}, {"x": 5, "y": 3}, {"x": 6, "y": 3}, {"x": 6, "y": 2}], "latency": "222", "head": {"x": 5, "y": 4}, "length": 4, "shout": "I'm not really sure...", "squad": ""}]}, "you": {"id": "snake-508e96ac-94ad-11ea-bb37", "name": "My Snake", "health": 54, "body": [{"x": 4, "y": 1}, {"x": 4, "y": 2}, {"x": 4, "y": 3}], "latency": "111", "head": {"x": 4, "y": 1}, "length": 3, "shout": "why are we shouting??", "squad": ""}}))
print(SnakeNeck({"game": {"id": "game-00fe20da-94ad-11ea-bb37", "ruleset": {"name": "standard", "version": "v.1.2.3"}, "timeout": 500}, "turn": 14, "board": {"height": 11, "width": 11, "food": [{"x": 5, "y": 5}, {"x": 9, "y": 0}, {"x": 2, "y": 6}], "hazards": [{"x": 3, "y": 2}], "snakes": [{"id": "snake-508e96ac-94ad-11ea-bb37", "name": "My Snake", "health": 54, "body": [{"x": 4, "y": 3}, {"x": 4, "y": 2}, {"x": 4, "y": 1}], "latency": "111", "head": {"x": 4, "y": 3}, "length": 3, "shout": "why are we shouting??", "squad": ""}, {
      "id": "snake-b67f4906-94ae-11ea-bb37", "name": "Another Snake", "health": 16, "body": [{"x": 5, "y": 4}, {"x": 5, "y": 3}, {"x": 6, "y": 3}, {"x": 6, "y": 2}], "latency": "222", "head": {"x": 5, "y": 4}, "length": 4, "shout": "I'm not really sure...", "squad": ""}]}, "you": {"id": "snake-508e96ac-94ad-11ea-bb37", "name": "My Snake", "health": 54, "body": [{"x": 4, "y": 3}, {"x": 4, "y": 2}, {"x": 4, "y": 1}], "latency": "111", "head": {"x": 4, "y": 3}, "length": 3, "shout": "why are we shouting??", "squad": ""}}))
