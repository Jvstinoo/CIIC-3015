def contains_duplicates(items1, items2):
    for i in items1:
        if i in items2:
            return True
    else:
        return False


print(contains_duplicates(['a', 'b', 'c', 'd'], ['p', 'q', 'r', 'c', 'x']))
print(contains_duplicates(['a', 'b', 'c', 'd'], ['p', 'q', 'r', 'x']))
