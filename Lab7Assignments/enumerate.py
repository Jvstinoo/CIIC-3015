'''Write a function called Enumerate() which duplicates the behavior of Python's 
builtin enumerate() generator without using it.'''


def Enumerate(arg):
    x = -1
    for i in arg:
        x += 1
        yield(i, x)


for x, i in Enumerate(range(2, 10+1, 2)):
    print(i, x)
