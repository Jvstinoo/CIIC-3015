def StrSplit(z, sep):
    '''counter = 0
    out = []
    for ct, i in enumerate(z):
        if i == sep:
            out.append(z[counter:ct])
            counter = ct+1
    out.append(z[counter:])
    return out'''
    out = []
    for i in z:
        if sep in i:
            out.append(i.split())
    return out


print(StrSplit('spam+sausage+eggs+spam+spam', '+'))
print(StrSplit("FUSspamROspam DAH", "spam"))
