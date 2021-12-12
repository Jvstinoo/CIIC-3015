def Cycle(d, key):
    if key not in d:
        return 0

    '''cycle = 1
  if key in d:
    new_key = d[key]
    while new_key != key and key in d:
      cycle += 1
      if new_key in d:
        new_key = d[new_key]
        continue
      else:
        cycle = 0
        break
  else:
    return 0
  return cycle'''


print(Cycle({'spam': 'eggs', 'eggs': 'bacon', 'bacon': 'spam',
      'sausage': 'biscuits', 'biscuits': 'milk'}, 'sausage'))
print(Cycle({'spam': 'eggs', 'eggs': 'bacon', 'bacon': 'spam',
      'sausage': 'biscuits', 'biscuits': 'milk'}, 'spam'))
print(Cycle({6: 'spam', 'spam': 3.5, 3.5: (1, 2),
      (1, 2): True, True: 6, False: False}, True))
print(Cycle({True: False, False: True}, False))
print(Cycle({'one': 'one'}, 17))
