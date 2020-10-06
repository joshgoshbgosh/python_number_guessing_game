import random
high_num = 100
low_num = 1
computerGuess = 50


mynumber = int(input("Pick a number between 1 and 100: "))
tries = 1


while computerGuess != mynumber:
    computerGuess = (low_num + high_num)//2
    if computerGuess > mynumber:
        print("Sorry to high!")
        high_num = computerGuess
        print(computerGuess)
    elif computerGuess < mynumber:
        print("Sorry to low!")
        low_num = computerGuess
        print(computerGuess)


    tries +=1

print("You did it! It only took you", tries, " tries!")
