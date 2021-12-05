def sum13(ls):
    if len(ls) == 0:
        return 0
    if ls[0] != 13:
        return sum13(ls[1:]) + ls[0]
    else:
        return sum13(ls[2:])


print(sum13([1, 2, 2, 1]))
print(sum13([13, 1, 2, 13, 2, 1, 13]))
print(sum13([1, 2, 13, 2, 1, 13]))
