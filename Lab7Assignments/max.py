'''Write a function called Max() which duplicates the behavior of Python's builtin max() without using it.
'''


def Max(something):
    thing = something[0]
    for i in something:
        if(i > thing):
            thing = i
    return thing


print(Max(range(100)))

print(Max([2.2, 6.6, 3.3, 4.4]))
