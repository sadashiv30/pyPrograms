"""
Write a program that generates a secret random number and asks the user to guess it.
It should count how many attempts were made before the number is guessed.
The program must also give hints to the user.
Example:
    python guess_a_number.py
    > Guess your number
    > 3
    > Wrong! Try with a larger one
    > 5
    > Wrong! Try with a smaller one
    > 4
    > You guessed correctly! The number was 4 indeed!
"""

magic = 34

def guess_a_number():
    count =0
    while(True):
        count+=1
    	num = int(raw_input("Guess your number"))
        if(num == magic):
            print "You guessed correctly! The number was  ", magic , "indeed!\n You took ", count , "chances to guess\n"
            break
        elif(num > magic):
            print "Wrong, try a lower number"
        else :
            print "Wrong, try a larger number"      
    return       