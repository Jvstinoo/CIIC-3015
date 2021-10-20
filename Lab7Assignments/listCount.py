def ListCount(z, n):
    out = 0

    for i in z:
        if(i == n):
            out += 1
    return out


print(ListCount([1, 2, 3], 3))
print(ListCount([], 2))
