def number_triangle(n):

    start = 1
    for num in range(start, n):
        print(f'{num}'*start)
        start += 1


number_triangle(6)
