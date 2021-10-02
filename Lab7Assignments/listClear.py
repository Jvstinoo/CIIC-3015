def ListClear(z):
    for i in z[:]:
        z.remove(i)
    return z


z = [1, 1, 1, 1, 1, 11, 1, 1, 1, 1, 1]
ListClear(z)
print(z)
