""" 
Day 2 
Turkish Ai Hub - Assignment 1 
@author: Mehmet Baran Munar
"""

# list of the odd numbers.
odd_list = [1,3,5,7,9,11]

# list of the even numbers.
even_list = [0,2,4,6,8,10]

# merging odd_list and even_list
new_list = odd_list + even_list

# multiplying all values of new_list by 2.
new_list = [2*i for i in new_list]

a = 0
# printing data types of all values.
for i in new_list:
    print(type(new_list[a]))
    a += 1
