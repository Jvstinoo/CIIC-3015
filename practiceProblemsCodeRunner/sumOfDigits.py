def sum_of_digits(n):
    while(n > 0):
        return n % 1000000//100000 + n % 100000//10000 + n % 10000//1000 + n % 1000//100 + n % 100//10 + n % 10//1
    return 0


print(sum_of_digits(827104))
print(sum_of_digits(0))


# Professor's Solution
def sum_of_nums(n):
    sum = 0

    while n != 0:

        digit = n % 10

        sum = sum + digit

        n = n // 10

    return sum


print(sum_of_nums(345))
