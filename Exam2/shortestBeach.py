def beach_dist(f):
    fhand = open(f)
    out = []
    dist = []

    for line in fhand:
        if not 'nb' in line:
            out.append(line.strip().split(',')[0])
            n = line.strip().split(',')[1]
            dist.append(n.split(' ')[0])
    shortest = min(dist)
    index = dist.index(shortest)

    return out[index]
