def calc_payi(dic, rate):
    out = dict()

    for key, value in dic.items():
        if value > 30:
            out[key] = value * rate[key] + 10
        else:
            out[key] = value * rate[key]
    return out
