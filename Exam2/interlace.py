def interlace(ls, ls2):
    out = []

    for j, i in enumerate(ls):
        out.append(ls2[j])
        out.append(ls[j])
    return out
