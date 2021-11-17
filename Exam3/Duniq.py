def Duniq(dic):
    out = dict()

    for k, v in dic.items():
        if tuple(dic.values()).count(v) <= 1:
            out[k] = v
    return tuple(sorted(out.keys()))


print(Duniq({'Eric': 'spam', 'Heidy': 'spam',
      'Yan': 'eggs', 'Maria': 'bacon', 'Jose': 'spam'}))
'''counter = dict()
    out = dict()
    tup = list()
    for i in dic.values():
        counter[i] = counter.get(i, 0) + 1

    for j, v in dic.items():
        out[v] = j

    for i, v in counter.items():
        if v == 1:
            tup.append(out[i])
    return tuple(sorted(tup))'''
