def Passwords(path):
    fopen = open(path)
    out = dict()

    for i in fopen:
        colon = i.find(':')
        out[i.split(':')[0]] = i[colon+1:].strip('\n')
    return out
