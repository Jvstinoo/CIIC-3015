'''When we define functions, we can use the return statement to return a value. However, sometimes it would be 
useful to return multiple values, and a tuple is the perfect structure to do so. Although we could accomplish the same 
thing with a list, but a list is a better fit if outside of the function call we still want to keep the values together, 
whereas a tuple is better if we're only "packaging" them together for the sake of returning multiple values.

Task
Write a function named min_max that receives a list of numbers as a parameter and returns a tuple that contains the 
minimum value and the maximum value (in that order) of the list. For example, if the list is [2, 5, 3.14, -6, 1], then 
the function should return (-6, 5).

Hint: You may use list functions or methods that you already know, but you must not modify the original list.'''


def min_max(n):
    new_list = sorted(n)
    return new_list[0], new_list[-1]


print(min_max([2, 4, 21, 2, 42, 2, -4]))
