'''Write a function called StrJoin() which takes two arguments, a string and an iterable, and duplicates
 the behavior of the builtin join() string method without using it.

'''


def StrJoin(n, z):
    out = ''
    stop = len(z)-1

    for i in z:
        if stop > 0:
            out += (i+n)
            stop -= 1
    out += z[-1]

    return out, stop


print(StrJoin('+', 'spam'))
print(StrJoin(' spam ', ['1', '2', '3', '4', '5']))
