"""
Define a function that asks for a string and echoes it back
until the input 'quit' is provided.
Example:
    echo()
    > Insert a string: hello
    > hello
    > Insert a string: world
    > world
    > Insert a string: quit
    > bye!
"""

def echo():
    while True:
        s = raw_input('Enter string : ')
        if s == 'quit':
            break
        else:
            print s
    print 'bye'