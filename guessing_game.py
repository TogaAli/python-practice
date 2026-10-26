#This is a simple guessing game. I imported random to  make the computer choose a random number within a given range. 
import random
goal=random.randint(1,10)

#Then made the user input their guesses.. 
guess=int(input("Guess the number!"))

#over and over until they got it right, with helpful message to help them know if they are getting closer.
while guess!=goal:
    if abs(guess-goal)<=2:
        print("You're close")
    else:
        print("Not quiet..")
    guess=int(input("Guess the number!"))

rint(f"You got it! The correct number is {goal}")
    
