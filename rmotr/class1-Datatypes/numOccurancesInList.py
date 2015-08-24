"""
Write a function that receives a list and an element and returns how many occurrences
of that particular element are in the list.
Example:
    occurrences([7, 1, 5, 8, 0, 7, 9, 1, 7], 7)  # The number 7 is repeated 3 times.
    > 3
Extras:
* Try with a for loop
* Try with a while loop
* Investigate special list methods or python libraries.
"""

def occurrences(a_list, an_element):
    count = 0
    for i in a_list:
      if(i==an_element):
        count+=1
        
    return count

def occurrences1(a_list, an_element):
    count = 0
    i = 0
    while(i != len(a_list)):
      if(a_list[i]==an_element):
        count+=1
      i+=1
        
    return count