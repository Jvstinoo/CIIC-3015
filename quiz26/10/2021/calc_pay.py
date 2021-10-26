def calc_pay(dic, dic2):
    out = dict()

    for key, value in dic.items():
        out[key] = dic[key] * dic2[key]

    return out


print(calc_pay({123456: 40, 987654: 30}, {123456: 7.25, 987654: 11.50}))
