def contains_duplicates(items):
    sum = 1
    out = 0
    while out < len(items):
        if(items[out] != items[sum]):
            return True
            out += 1
            sum += 1
        else:
            return False


print(contains_duplicates(['a', 'b', 'c', 'd']))
print(contains_duplicates(['a', 'b', 'c', 'd', 'a']))
