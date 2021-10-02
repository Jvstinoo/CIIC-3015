def ListIndex(z, n):
    mew = 0

    for i in z:
        if(i != n):
            mew += 1
        else:
            return mew
    return mew


print(ListIndex([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1], 2))
print(ListIndex([1, 2, 3], 3))
print(ListIndex(['spam', 'eggs', 'sausage', 'bacon', 'spam'], 'spam'))
