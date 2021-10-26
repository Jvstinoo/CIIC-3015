def AlmostMin(c):

    return list(set(c))[1]


print(AlmostMin((4, 4, 2, 2, 2)))
print(AlmostMin(('spam', 'spam', 'spam', 'eggs', 'bacon', 'spam')))
print(AlmostMin(range(30, 0, -1)))
