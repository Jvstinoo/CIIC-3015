'''Write a function called IsSorted() which takes a list as a parameter and returns True if all 
of the elements in that list are in sorted order, False if they are not. The elements in the list may 
be of any type. Two sequential values (a,b) are defined to be in sorted order if and only if a <= b.

'''


def IsSorted(list):
    '''sorted = list[:]
    sorted.sort()
    if(sorted == list):
        return True
    return False
'''
    return (list == sorted(list))


print(IsSorted(['bacon', 'eggs', 'spam', 'spam', 'spam', 'spam', 'spam']))
print(IsSorted([2, 1, 3, 4, 5]))

print(IsSorted(['bacon', 'eggs', 'spam', 'spam', 'spam', 'spam', 'spam']))
print(IsSorted([1, 2, 3, 4, 5, 6, 7, 9, 8]))
