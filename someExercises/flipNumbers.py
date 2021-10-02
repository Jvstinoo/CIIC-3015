

def swap_adjacent(numList):

    for i in numList(0, 2):
        numList[i] = numList[-1]
    return numList


numList = [0, 2, 4, 6]
swap_adjacent(numList)
print(numList)
