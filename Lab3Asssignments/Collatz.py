'''def Collatz(n):
    times = 0              # Counter to keep track of the times n // or *
    while n > 1:
        if(n % 2 == 0):    # Check if n is divisible by 2
            n = n//2
        else:              # If not
            n = n*3+1

        times += 1         # Finally add 1 if any of the above get completed

    return times


print(Collatz(4))
'''


def Collatz(n):
    loops = 0
    while n != 1:
        loops += 1
        if (n % 2) == 0:
            n //= 2
            continue
        else:
            n = n*3+1
            continue
    return loops


print(Collatz(931386509544713451))
