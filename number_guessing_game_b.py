import random

mynumber = int(input("Pick a number between 1 and 100: "))
tries = 1
computerGuess = random.randint(1, 100)

while computerGuess != mynumber:
    if tries > 10:
        print("Game Over!")
        break
    elif computerGuess != mynumber:
        print("Sorry thats not it!")
        computerGuess = random.randint(1, 100)
        print(computerGuess)

    tries +=1

else:
    print("You did it! It only took you", tries, " tries!")
