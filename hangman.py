import random
with open ('/usr/share/dict/words') as infile:
    words = infile.read().split()
random_word = random.choice(words)
print(random_word)
