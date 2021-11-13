def ListCount(ls, r):
    if len(ls) == 0:
        return 0
    if ls[0] == r:
        return ListCount(ls[1:], r) + 1
    else:
        return ListCount(ls[1:], r)
