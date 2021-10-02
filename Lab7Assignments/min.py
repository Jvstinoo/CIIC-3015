def Min(something):
    thing = something[0]
    for i in something:
        if(i < thing):
            thing = i
    return thing


print(Min(range(100)))
print(Min([False, True]))
