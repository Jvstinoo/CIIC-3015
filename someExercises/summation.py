'''Write a function called Summation() that accepts two integers m and n (where m ≤ n)
 and returns the sum of all numbers from m to n. For example,  with m=2 and n=6 it should
  return 20, since 2 + 3 + 4 + 5 + 6 = 20

Notes: You can assume that the first number will be less than or equal to 
the second number. You must use loops.
'''
# Summation Exercise


def Summation(m, n):
    total = 0
    for i in range(m, n+1):
        total += i
    return total


print(Summation(2, 6))
print(Summation(10, 13))
print(Summation(-5, 5))


# Sum each Digit exercise

def SumOfDigits(n):
    total = 0
    while(n != 0):
        unit = n % 10
        total += unit
        n //= 10
    return total


print(SumOfDigits(827104))
