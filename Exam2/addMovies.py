def add_movies(N):
    out = []

    for i in range(N):
        inp = input('Add the new movie :')
        out.append(inp)
    return out


N = int(input('number of movies you want to add :'))

print(add_movies(N))
