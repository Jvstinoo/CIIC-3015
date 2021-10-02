'''Write a function called StrJoin() which takes two arguments, a string and an iterable, and duplicates
 the behavior of the builtin join() string method without using it.

'''


def StrJoin(n, z):
    result = ''
    out = 0

    for i in z[:]:
        z[out] += n
        out += 1
    return z


print(StrJoin('+', 'spam'))
