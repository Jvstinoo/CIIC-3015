def invert_dict(dic):

    cop = dic.copy()
    out = dict()

    for keys, values in cop.items():
        out[values] = keys

    return out


print(invert_dict({'Justin': 'Name', 'Balbuena': 'Second Name'}))
