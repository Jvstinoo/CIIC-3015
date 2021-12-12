'''The dot product of two vectors is calculated by multiplying the corresponding elements of each 
vector together and summing those products. For example, the dot product of 
[2, 0, 1] and [6, 3, 4] = 2*6 + 0*3 + 1*4 = 12 + 0 + 4 = 16

Write a function called Dot() which takes two lists as arguments and returns 
the dot product of those lists as a float. You may assume that both lists have equal 
length and contain only numeric values.

Hint: Use a while-loop here, not a for-loop. (Why?)

Also: We want you to roll your own loops here. Do not import a module like numpy to do the work for you.'''


def Dot(l1, l2):
    '''sum = 0
    out = 0
    while out < len(l1):
        mult = l1[out] * l2[out]
        sum += mult
        out += 1
    return float(sum)
'''

    return sum()


print(Dot([1, 0, 2, 0, 3, 0], [0, 1, 0, 2, 1, 3]))
print(Dot([3], [-4]))
print(Dot([2, 3, 2, 3], [1, 1, -1, -1]))
print(Dot([], []))
