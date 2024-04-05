import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = list(random.choice(word_list))
letter = input('Please guess a letter: ').lower()

for guess in chosen_word:
    if letter == guess:
        print('right')
    else:
        print('wrong')