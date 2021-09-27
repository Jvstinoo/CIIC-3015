'''Write a function named remove_value that has three parameters: a list of ints called int_list, an int parameter called remove, 
and another int parameter called times. 

The function should return a new list with up to times occurrences of remove, removed. 

For example, the call to remove_value([1,4,3,6,4,3,2,4,8,11], 4, 2) should remove the number 4 from the list, up to 2 times. 
It should return [1,3,6,3,2,4,8,11]. Notice that we only removed the first 2 occurrences of the number 4 in the list!


int_list can be empty, and can contain negative numbers

remove can be any integer, including negative numbers

times must be 0 or greater. If it is less than or equal to zero, return the original list, since there's no need to remove any values. 


Hint: Create a variable result initialized to an empty list. You can iterate over the first parameter (the list) 
and check each value to see if we want to keep it. But you'll also need a way to keep track of how many times you've removed values, 
to account for the 3rd parameter (Think about where you want to keep track of this, you'll need to create it, check it, and increment it). 

If you decide to keep the value, don't forget to append the element at the current index to result.
'''


def remove_value(int_list, remove, times):
    result = []

    removed = 0


print(remove_value([1, 4, 3, 6, 4, 3, 2, 4, 8, 11], 4, 2))
print(remove_value([11], 11, 0))
