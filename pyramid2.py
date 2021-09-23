def print_pyramid(n):
    for i in range(0, n):
        line = '*'
        for j in range(0, i):
            line += '*'
        print(line)


print_pyramid(6)
