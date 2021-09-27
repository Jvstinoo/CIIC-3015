def prime_numbers(n):

    result = []
    for i in range(0, n+1):
        if i > 1:
            for j in range(2, i):
                if(i % j == 0):
                    break
            else:
                result.append(i)
    return result


print(prime_numbers(10))
'''

Proffesor's Solution:

def is_prime(num):
    numDivisible = 0
    # check if the number is
    # divisible by any number
    # from 2 to (number - 1)
    # If it is, it is not prime.
    for i in range(2, num):
        if num % i == 0:
         return False
    return True
        
def prime_numbers(nums):
    ans = list()
    for n in range(2, nums + 1):
        if is_prime(n):
            ans.append(n)
    return ans   
        '''
