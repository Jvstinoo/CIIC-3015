'''
This is a variation of an infamous tech interview question. 
Write a function called FizzBuzz() which takes an integer argument. 
If that integer is evenly divisible by 3, return the string "Fizz". 
If that integer is evenly divisible by 5, return the string "Buzz". 
And if the integer is evenly divisible by both 3 and 5, return the string "FizzBuzz". 
Otherwise just return the integer.

Note: This problem is all over the internet. 
It would take you three seconds to look up a solution. 
Please don't, this is a good test of your ability to think logically with conditionals.
'''


def FizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"

    return n


print(FizzBuzz(7))
