def number_triangle(n):

    start = 1
    for num in range(start, n+1):
        print(f'{num}'*start)
        start += 1


number_triangle(6)
