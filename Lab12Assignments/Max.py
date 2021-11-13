def Max(cont):
    if len(cont) == 1:
        return cont[0]
    out = Max(cont[1:])
    if cont[0] > out:
        return cont[0]
    else:
        return out


print(Max((2.2, 6.6, 3.3, 4.4)))
print(Max(range(100)))
