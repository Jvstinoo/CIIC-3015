def even_numbers(ls):
    for i in ls:
        if(i % 2) == 0:
            pass
        else:
            ls.remove(i)
    ls.sort()

    return ls


print(even_numbers([2, 5, 4, 8, 3, 6, 7]))
print(even_numbers([12, 20, 40, 10, 6, 9, 5, 4, 1]))
