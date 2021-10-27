def MergeSums(dic, dic2):
    out = dict(dic2)

    for key, values in dic.items():
        if key in dic2:
            out[key] = values + dic2[key]
        else:
            out[key] = values

    return out


A = {'spam': 10, 'eggs': 0, 'bacon': 1}
B = {'sausage': 1, 'spam': 6, 'eggs': 2}
print(len(MergeSums(A, B)))
print(len(A), len(B))
