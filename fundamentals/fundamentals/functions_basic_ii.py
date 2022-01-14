# exc 1 Countdown - 
import re


def count_it_down(num):
    list = []
    # for x in range(num,0,-1):
    for x in range(num,-1,-1):
        list.append(x)
    return list

print(count_it_down(5))


# exc 2 Print and Return
def print_return(provided):
    print(provided[0])
    return provided[1]

print(print_return([1,2]))

# exc 3 First Plus Length
def f_p_l(list):
    # return list[0] + list.length
    return list[0] + len(list)

print(f_p_l([3,4,2,6,7,11]))

# exc 4 values greater than second
"""Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
"""
def list_in(list):
    val_chk = list[1]
    new_list = []
    count = 0
    for x in list:
        if x > val_chk:
            new_list.append(x)
            count += 1
    print(count)
    return new_list

print(list_in([4,6,8,2,5,9]))
        

# exc 5 this length, that value
"""Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
Example: length_and_value(4,7) should return [7,7,7,7]"""

def David(size,value):
    return_list = []
    for x in range(size):
        return_list.append(value)
    return return_list

print(David(4,7))