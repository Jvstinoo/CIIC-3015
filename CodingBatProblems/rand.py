'''Function to check if a 2 is next to another 2'''


def has22(ls):
    if len(ls) == 0:
        return False
    if ls[0] == 2 and ls[1] == 2:
        return True
    else:
        return has22(ls[1:])


print(has22([2, 2]))
