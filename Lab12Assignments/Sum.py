def Sum(cont):
    if len(cont) == 1:
        return cont[0]
    return cont[0] + Sum(cont[1:])


print(Sum(range(5)))
