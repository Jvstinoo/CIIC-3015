def IsSorted(ls):
    if len(ls) <= 1:
        return True
    if ls[0] > ls[1]:

        return False
    else:
        return IsSorted(ls[1:])


print(IsSorted([4, 3, 2, 43]))
print(IsSorted([1, 2, 3]))
