def last2(str):
    counter = 0

    for i in range(len(str[2:-2])-1):
        if str[i] == str[i+1] and str[i]:
            counter += 1
        elif str[i] == str[i+1] and str[i]:
            counter += 1
    if str[:2] == str[-2:]:
        counter -= 1

    return counter


print(last2('hixxxxxxhi'))
print(last2('xaxxaxaxx'))
print(last2('xxaxxaxxaxx'))
