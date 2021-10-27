def merge(arg, arg2):
    out = dict()

    for val, i in enumerate(arg):
        out[i] = arg2[val]
    return out


def merge(arg, arg2):

    return dict(zip(arg, arg2))


print(merge((1, 2, 3), ('a', 'b', 'c')))
