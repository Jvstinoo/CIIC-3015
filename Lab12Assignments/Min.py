def Min(cont):
    if len(cont) == 1:
        return cont[0]
    if cont[0] < Min(cont[1:]):
        return cont[0]
    else:
        return Min(cont[1:])
