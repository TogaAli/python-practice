import random

goal=random.randint(1,10)
guess=int(input("Guess the number!"))

while guess!=goal:
    if abs(guess-goal)<=2:
        print("You're close")
    else:
        print("Not quiet..")
    guess=int(input("Guess the number!"))

rint(f"You got it! The correct number is {goal}")
    
