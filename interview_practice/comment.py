# this code is showing comment and print basic variable 

"""
this is docstring i don't know how to
use it properly i will learn about it
"""
first = 3
second = 5
sum_of_both = first + second
print(sum_of_both)

name = 'anshul' 
surname = 'gera' 
fullname = "my name is " + name + " "+ surname
print(fullname)

def unique(list1): 
    # intilize a null list 
    unique_list = []   
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    # print list 
    for x in unique_list: 
        print (x)

store = [2, 3, 1, 4, 5, 5, 6, 7, 7]
store.sort()
store.reverse()
print(unique(store))