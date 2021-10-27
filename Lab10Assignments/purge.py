def Purge(dic, val):

    newDic = dict(dic)
    for key, values in newDic.items():
        if values == val:
            del dic[key]


G = {1: True, 2: False, 3: True, 4: False, 5: True, 6: False, 7: True, 8: True}
Purge(G, False)
print(len(G), G[1], G[3], G[5], G[7], G[8])
