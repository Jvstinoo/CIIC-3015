def ListCount(ls, r):
    if len(ls) == 0:
        return 0
    elif ls[0] == r:
        return 1 + ListCount(ls[1:], r)

    else:
        return ListCount(ls[1:], r)


print(ListCount([1, 1, 1, 1, 1, 1, 1, 1], 1))
print(ListCount([], 6))
print(ListCount([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1], 1))
