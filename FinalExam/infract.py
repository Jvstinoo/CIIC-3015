def infract_det(fname):
    fopen = open(fname)
    out = dict()

    for lines in fopen:
        semi_colon = lines.find(':')
        comma = lines.find(',')
        out[lines[0]] = (lines[semi_colon+1:comma+1], lines[comma+2:].strip())

    return out.get(max(out.keys()))


print(infract_det('infract.txt'))
