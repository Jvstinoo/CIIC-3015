import math


def Primes():
    i = 2
    while True:
        for j in range(2, int(math.sqrt(i) + 1)):
            if i % j == 0:
                break
        else:
            yield i
        i += 1


def CountUniquePrimeFactors(n):
    out = set()
    for i in Primes():
        if i > n:
            break
        if n % i == 0:
            out.add(i)
    return len(out)


print(CountUniquePrimeFactors(12))
