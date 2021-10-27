def Inventory(path):
    fopen = open(path)
    out = dict()

    for i in fopen:
        if i.strip() not in out:
            out[i.strip()] = 1
        else:
            out[i.strip()] += 1
    return out


print(Inventory('s.txt'))
