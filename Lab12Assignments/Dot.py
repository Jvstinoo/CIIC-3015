def Dot(ls, ls2):
    if len(ls) == 0:
        return 0.0
    else:
        return Dot(ls[1:], ls2[1:]) + ls[0] * ls2[0]


print(Dot([1, 0, 2, 0, 3, 0], [0, 1, 0, 2, 1, 3]))
print(Dot([1, 2, 3], [1, 1, 1]))
