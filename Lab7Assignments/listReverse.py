def ListReverse(ls):
    for i in ls[::-1]:
        ls.append(i)
        ls.remove(i)
    return ls


print(ListReverse([1, 2, 3]))
print(ListReverse([1, 1, 1, 1, 1, 1, 1, 1, 2]))
