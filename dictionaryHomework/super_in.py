def super_in(dic, s):

    if s in dic.values() or s in dic.keys():
        return True
    return False


print(super_in({'a': 1, 'b': 2, 'c': 3}, 'a'))
