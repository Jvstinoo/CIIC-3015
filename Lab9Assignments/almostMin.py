def AlmostMin(container):
    smallest = None

    for i in range(len(container)):
        if container[i] < container[i+1]:
            smallest = container[i]
    return smallest


print(AlmostMin((2, 2, 4, 4, 4)))
