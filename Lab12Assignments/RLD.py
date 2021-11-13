def RLD(s):
    if len(s) == 0:
        return ''
    else:
        return str(int(s[0]) * s[1]) + RLD(s[2:])


print(RLD('57'))
print(RLD('1A3C1b'))
