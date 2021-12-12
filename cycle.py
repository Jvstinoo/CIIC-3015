'''The cycle length of a dictionary and an initial key is a completely made-up term that we shall define as follows:

Starting with our initial key, look up its associated value in the dictionary. That value becomes our next key. Now look up that next key in the dictionary to get the next associated value which becomes the next key after that, and so on. If at any point we are unable to find a key within our dictionary, the cycle length is defined to be zero. If at any point we compute a next key which equals our initial key, the cycle length is defined to be the total number of unique keys that we have used. Which is to say, we have found a loop and the cycle length is the length of that loop.

Example:

D = { 'spam':'eggs', 'eggs':'bacon', 'bacon':'spam', 'sausage':'biscuits', 'biscuits':'milk' }

The cycle length of D with an initial key of 'spam' would equal three because we have a cycle of 'spam' > 'eggs' > 'bacon' which then repeats back to 'spam' again. So, three keys in all. Initial keys of 'eggs' or 'bacon' would also result in cycle lengths of three since both of those keys are also part of that same loop. However, the cycle length of D with an initial key of 'sausage' or 'biscuits' or 'milk' would equal zero since none of those keys are part of a loop.

Write a function called Cycle() which takes a dictionary and an initial key as arguments, and returns the cycle length of that combination as defined above. You may assume that no two keys map to identical values.'''


def cycle(d, key):
    count = 0
    while key in d:
        count += 1
        key = d[key]
    return count
