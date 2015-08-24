"""
Write a function that receives a string and returns a camel case version of it.
Example:
    camel_case('hello world')  # Hello World
"""

def camel_case(a_string):
    i=0
    changecase=1
    b_string=''
    for i in a_string:
        if(changecase==1):
            if(i>='a' and i<='z'):
                b_string+=i.upper()
                changecase=0
            else:
                changecase=0
                b_string+=i
        elif(i==' '):
        	b_string+=i
        	changecase=1
        else:
            b_string+=i
            changecase=0
        
    return b_string