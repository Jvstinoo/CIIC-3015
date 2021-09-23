'''Create a function called multiples that receives a number to calculate its multiples and how many multiples they 
want to obtain. Your function must return a list that contains the multiples.

Perform your development in the following embedded Repl.it IDE, but copy your final code into the text
 area further below labeled "Answer".'''


def multiples(n, stop):
    multiple = []
    for i in range(0, n*stop+1, n):
        multiple.append(i)
    return(multiple)


print(multiples(4, 5))
print(multiples(3, 6))
print(multiples(8, 2))
