def SnakeTargets(dic):
    return [i.get('name') for i in dic['board']['snakes'] if i.get('length') < dic['you']['length']]


print(SnakeTargets({"game": {"id": "game-00fe20da-94ad-11ea-bb37", "ruleset": {"name": "standard", "version": "v.1.2.3"}, "timeout": 500}, "turn": 14, "board": {"height": 11, "width": 11, "food": [{"x": 5, "y": 5}, {"x": 9, "y": 0}, {"x": 2, "y": 6}], "hazards": [{"x": 3, "y": 2}], "snakes": [{"id": "snake-508e96ac-94ad-11ea-bb37", "name": "My Snake", "health": 54, "body": [{"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0}], "latency": "111", "head": {"x": 0, "y": 0}, "length": 3, "shout": "why are we shouting??", "squad": ""}, {
      "id": "snake-b67f4906-94ae-11ea-bb37", "name": "Another Snake", "health": 16, "body": [{"x": 5, "y": 4}, {"x": 5, "y": 3}, {"x": 6, "y": 3}], "latency": "222", "head": {"x": 5, "y": 4}, "length": 3, "shout": "I'm not really sure...", "squad": ""}]}, "you": {"id": "snake-508e96ac-94ad-11ea-bb37", "name": "My Snake", "health": 54, "body": [{"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0}], "latency": "111", "head": {"x": 0, "y": 0}, "length": 3, "shout": "why are we shouting??", "squad": ""}}))
print(SnakeTargets({"game": {"id": "game-00fe20da-94ad-11ea-bb37", "ruleset": {"name": "standard", "version": "v.1.2.3"}, "timeout": 500}, "turn": 14, "board": {"height": 11, "width": 11, "food": [{"x": 5, "y": 5}, {"x": 9, "y": 0}, {"x": 2, "y": 6}], "hazards": [{"x": 3, "y": 2}], "snakes": [{"id": "snake-508e96ac-94ad-11ea-bb37", "name": "My Snake", "health": 54, "body": [{"x": 8, "y": 0}, {"x": 7, "y": 0}, {"x": 6, "y": 0}], "latency": "111", "head": {"x": 8, "y": 0}, "length": 3, "shout": "why are we shouting??", "squad": ""}, {
      "id": "snake-b67f4906-94ae-11ea-bb37", "name": "Another Snake", "health": 16, "body": [{"x": 5, "y": 4}, {"x": 5, "y": 3}], "latency": "222", "head": {"x": 5, "y": 4}, "length": 2, "shout": "I'm not really sure...", "squad": ""}]}, "you": {"id": "snake-508e96ac-94ad-11ea-bb37", "name": "My Snake", "health": 54, "body": [{"x": 8, "y": 0}, {"x": 7, "y": 0}, {"x": 6, "y": 0}], "latency": "111", "head": {"x": 8, "y": 0}, "length": 3, "shout": "why are we shouting??", "squad": ""}}))
print(SnakeTargets({"game": {"id": "game-00fe20da-94ad-11ea-bb37", "ruleset": {"name": "standard", "version": "v.1.2.3"}, "timeout": 500}, "turn": 14, "board": {"height": 11, "width": 11, "food": [{"x": 5, "y": 5}, {"x": 9, "y": 0}, {"x": 2, "y": 6}], "hazards": [{"x": 3, "y": 2}], "snakes": [{"id": "snake-508e96ac-94ad-11ea-bb37", "name": "My Snake", "health": 54, "body": [{"x": 4, "y": 1}, {"x": 4, "y": 2}, {"x": 4, "y": 3}], "latency": "111", "head": {"x": 4, "y": 1}, "length": 3, "shout": "why are we shouting??", "squad": ""}, {"id": "snake-b67f4906-94ae-11ea-bb37", "name": "Another Snake", "health": 16, "body": [{"x": 5, "y": 4}, {"x": 5, "y": 3}, {"x": 6, "y": 3}, {"x": 6, "y": 2}], "latency": "222", "head": {"x": 5, "y": 4}, "length": 4, "shout": "I'm not really sure...", "squad": ""}, {
      "id": "snake-b67f4906-94ae-11ea-bb37", "name": "Yet Another Snake", "health": 16, "body": [{"x": 5, "y": 4}, {"x": 5, "y": 3}], "latency": "222", "head": {"x": 5, "y": 4}, "length": 2, "shout": "I'm not really sure...", "squad": ""}, {"id": "snake-b67f4906-94ae-11ea-bb37", "name": "Yet Another Other Snake", "health": 16, "body": [{"x": 5, "y": 4}, {"x": 5, "y": 3}], "latency": "222", "head": {"x": 5, "y": 4}, "length": 2, "shout": "I'm not really sure...", "squad": ""}]}, "you": {"id": "snake-508e96ac-94ad-11ea-bb37", "name": "My Snake", "health": 54, "body": [{"x": 4, "y": 1}, {"x": 4, "y": 2}, {"x": 4, "y": 3}], "latency": "111", "head": {"x": 4, "y": 1}, "length": 3, "shout": "why are we shouting??", "squad": ""}}))


print(SnakeTargets({"game": {"id": "game-00fe20da-94ad-11ea-bb37", "ruleset": {"name": "standard", "version": "v.1.2.3"}, "timeout": 500}, "turn": 14, "board":
                    {"height": 11, "width": 11, "food": [{"x": 5, "y": 5}, {"x": 9, "y": 0}, {"x": 2, "y": 6}], "hazards": [{"x": 3, "y": 2}], "snakes": [{"id": "snake-508e96ac-94ad-11ea-bb37",
                                                                                                                                                           "name": "My Snake", "health": 54, "body": [{"x": 4, "y": 3}, {"x": 4, "y": 2}, {"x": 4, "y": 1}, {"x": 4, "y": 0}, {"x": 3, "y": 0}], "latency": "111", "head": {"x": 4, "y": 3},
                                                                                                                                                           "length": 5, "shout": "why are we shouting??", "squad": ""}, {
                        "id": "snake-b67f4906-94ae-11ea-bb37", "name": "Solid Snake", "health": 16, "body": [{"x": 5, "y": 4}, {"x": 5, "y": 3}, {"x": 6, "y": 3}, {"x": 6, "y": 2}], "latency": "222",
                        "head": {"x": 5, "y": 4}, "length": 4, "shout": "I'm not really sure...", "squad": ""}]}, "you": {"id": "snake-508e96ac-94ad-11ea-bb37", "name": "My Snake", "health": 54, "body":
                                                                                                                          [{"x": 4, "y": 3}, {"x": 4, "y": 2}, {"x": 4, "y": 1}, {"x": 4, "y": 0}, {"x": 3, "y": 0}], "latency": "111", "head": {"x": 4, "y": 3}, "length": 5, "shout": "why are we shouting??",
                                                                                                                          "squad": ""}}))
