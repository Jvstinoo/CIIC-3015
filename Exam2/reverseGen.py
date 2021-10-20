def Reverse(container):
    inverse = container[:]
    for i in reversed(inverse):
        yield i


print(list(Reverse('spam')))
print(list(Reverse('spam')))
