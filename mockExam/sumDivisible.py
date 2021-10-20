def sum_divisible(n):

    out = 0

    for i in range(5, n+1):
        if i % 5 == 0:
            out += i

    return out


print(sum_divisible(15))
