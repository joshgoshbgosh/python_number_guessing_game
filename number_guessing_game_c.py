import random
high_num = 100
low_num = 1


mynumber = int(input("Pick a number between 1 and 100: "))
tries = 1
computerGuess = random.randint(low_num, high_num)

while computerGuess != mynumber:
    computerGuess = random.randint(low_num, high_num)
    if tries > 5:
        print("Game Over!")
        break
    elif computerGuess > mynumber:
        print("Sorry to high!")
        high_num = computerGuess
        print(computerGuess)
    elif computerGuess < mynumber:
        print("Sorry to low!")
        low_num = computerGuess
        print(computerGuess)


    tries +=1

else:
    print("You did it! It only took you", tries, " tries!")
