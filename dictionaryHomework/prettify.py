def prettify(dic):
    out = ''

    for key, value in dic.items():
        out += (f'({key}:{value}),')
    return out[:-1]
