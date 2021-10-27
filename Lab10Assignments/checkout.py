def Checkout(dic, dic2):
    out = 0.0

    for key, value in dic.items():
        if key in dic2:
            out += (dic[key]*dic2[key])
    return out


price = {'spam': 9.00, 'eggs': 3.00, 'bacon': 5.00, 'sausage': 4.50}
order = {'spam': 100, 'chocolate': 3, 'eggs': 1}
print(Checkout(price, order))
