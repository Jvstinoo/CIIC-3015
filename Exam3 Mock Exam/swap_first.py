def swap_first(ls, ls2):
    outLs = list()
    outLs2 = list()

    for i in range(len(ls)):
        outLs.append((ls2[i][0], ls[i][1]))
        outLs2.append((ls[i][0], ls2[i][1]))
    print(outLs)
    print(outLs2)
