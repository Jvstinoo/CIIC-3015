'''Write a function called IsWithinEpsilon() which takes three 
numeric arguments and returns True or False depending on whether 
the distance between the first number and the second number is less 
than or equal to the third number. Your function should give identical
 results regardless of the order of the first two arguments.'''


def IsWithinEpsilon(a, b, c):
    # New solution
    return (abs(a-b) <= c)
    # Init solution
    '''if abs(a - b) <= c:
        return True
    else:
        return False'''


# check if the distance between a and b is lesser than c or something
print(IsWithinEpsilon(2.1, 2.3, 0.22))
print(IsWithinEpsilon(2.2, 2.1, 0.08))
