import math
'''function that generates prime numbers'''


def Primes():
    i = 2
    while True:
        for j in range(2, int(math.sqrt(i) + 1)):
            if i % j == 0:
                break
        else:
            yield i
        i += 1
