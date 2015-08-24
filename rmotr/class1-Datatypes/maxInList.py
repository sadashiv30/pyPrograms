"""
Write a function that receives a list and returns the larger number in the list.
Example:
    max_in_list([7, 1, 5, 8, 0, 7, 9, 1, 7])
    > 9

Extras:
* Try with a for loop
* Try with a while loop
* Investigate special list methods or python libraries.
"""

def max_in_list(a_list):
    max = 0
    for i in a_list:
        if(i > max):
        	max = i
    return max
    
def max_in_list2(a_list):
    max = 0
    i =0
    while(i!= len(a_list)):
        if(a_list[i] > max):
        	max = a_list[i]
        i+=1
    return max

def max_in_list3(a_list):
    return max(a_list)