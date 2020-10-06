# random number guessing game

import random

print ("Do you want to play a game??? You will only survive if you choose wisely. \n You only have 5 tries.  Good Luck!")

randomNumber = random.randint(1, 100)  #randint selects a random number from the specified numbers 1-99.

guess = int(input("enter a number between 1 and 100: "))
tries = 1


while (guess != randomNumber):
    if tries > 5:        #number of tries available to beat the game
        print("You did not choose wisely! It was", randomNumber)
        break
    elif guess < randomNumber:
        print ("To Low")
    elif guess > randomNumber:
        print ("To High")

    guess = int(input("Guess Again:"))
    tries +=1   #this is counting tries being used.

else:
    print ("You are wise!")
