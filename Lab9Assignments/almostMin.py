def AlmostMin(container):
    ls = list(set(container[:]))
    ls.remove(min(ls))

    if len(ls) > 1:
        return min(ls)
    return None


print(AlmostMin(('spam', 'spam', 'spam', 'eggs', 'bacon', 'spam')))
print(AlmostMin(range(30, 0, -1)))

print(AlmostMin([1, 1, 1, 1, 1, 1, 1, 1]))
