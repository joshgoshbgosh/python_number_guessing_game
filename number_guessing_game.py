# random number guessing game

import random

print ("Do you want to play a game??? You will only survive if you choose wisely. You only have 5 tries.  Good Luck!")

randomNumber = random.randint(1, 99)  #randint selects a random number from the specified numbers 1-99.

guess = int(input("enter a number between 1 and 99: "))
tries = 1

while (guess != randomNumber):
    if tries > 5:
        print("You did not choose wisely!")
        break
    elif guess < randomNumber:
        print ("To Low")
    elif guess > randomNumber:
        print ("To High")

    guess = int(input("Guess Again:"))
    tries +=1

else:
    print ("You are wise!")
