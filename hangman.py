import random
with open ('/usr/share/dict/words') as infile:
    words = infile.read().split()
random_word = random.choice(words).lower().replace("\n", "")

used_characters = []
guess_word = []   #setting up my empty list for letters and word
len_word = len(random_word) #assigning length and random_word to len_word

def display():
    for char in random_word:
        guess_word.append('_') #this seperates the word to look like this - - - - - - - - -
    print("The word has ", len_word, "letters.")
    return guess_word

def play():
    turns = 20
    while turns > 0:      #creating amount of tries and keeping up with amount left
        print(turns, "guesses left")
        print(guess_word)
        if '_' not in guess_word:
            print("You got!")
            break

        letter_guessed = (input("Guess a letter >")).lower()
        if letter_guessed in used_characters:
            print ("Already picked this one...")
        else:
            turns -= 1      #here is saying if a letter is already picked  to notify and take away tries.
        if turns >= 1:
            print ("Keep going!")
        if turns == 0:
            print("Game Over!")
            print("Word was", random_word)
        for letter in range(0, len_word):
            if random_word[letter] == letter_guessed:
                guess_word[letter] = letter_guessed
display()
play()
