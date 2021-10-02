def flip_sign(ls):
    for i in ls:
        if(i < 0):
            i = abs(i)

    return ls


    # return [-i for i in ls]
print(flip_sign([0, -2, 4, -1, -1]))
