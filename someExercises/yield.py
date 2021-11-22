def Prompt():
    while True:
        x = input('Enter an integer of "Done": ')
        if x.lower() == 'done':
            break
        yield int(x)


sum = 0
for val in Prompt():
    sum += val
