#EX-6 : GUESS THE NUMBER 

#PROBLEM : MAKE GUESS THE NUMBER GAME USING LOOPS

#SOLUTION:
import random
n=random.randint(1,30)

print("guess the number between 1 to 30 in 5 chance")
chance=0


while chance<5:
    inp=int(input("guess the number\n"))
    if chance==4:
        print("game over")
        break
    if inp>n:
        print("your guess is too high\nnumber of attempt",chance+1)
    elif inp<n:
        print("your guess is too low\nnumber of attempt",chance+1)
    else :
        print("you guess the correct number\nnumber of attempt",chance+1)
        break
    chance=chance+1

#OUTPUT :
"""
guess the number between 1 to 30 in 5 chance
guess the number
20
your guess is too low
guess the number     
21
your guess is too low
guess the number     
22
your guess is too low
guess the number
25
your guess is too low
guess the number
30
game over
"""

#                                  """END"""
