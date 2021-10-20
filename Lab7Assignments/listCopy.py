def ListCopy(z):
    '''y = list()

    for i in z:
        y.append(i)
    return y'''

    return [i for i in z]


print(ListCopy([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1]))
