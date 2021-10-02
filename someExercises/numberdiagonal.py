def number_diagonal(n):
    spaces = ''

    for i in range(1, n+1):
        print(f'{spaces}' + str(i))
        spaces += ' '


print(number_diagonal(10))
