def ReadDict(f):
    fopen = open(f)
    out = dict()

    for j, lines in enumerate(fopen):
        separated = (lines.strip().split(',')[:])
        for i in separated:
            out[i.split(':')[0]] = i.split(':')[1]
    return out
    fopen.close()
