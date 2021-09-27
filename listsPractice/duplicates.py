def contains_duplicates(items):
    search = []
    for i in items:
        if(i not in search):
            search.append(i)

        else:
            return True
    return False


print(contains_duplicates(['a', 'b', 'c', 'd']))
print(contains_duplicates(['a', 'b', 'c', 'd', 'a']))
