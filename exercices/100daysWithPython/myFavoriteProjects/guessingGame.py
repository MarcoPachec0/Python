import random

print(r"""   _____                     _                _____                      
  / ____|                   (_)              / ____|                     
 | |  __ _   _  ___  ___ ___ _ _ __   __ _  | |  __  __ _ _ __ ___   ___ 
 | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` | | | |_ |/ _` | '_ ` _ \ / _ \
 | |__| | |_| |  __/\__ \__ \ | | | | (_| | | |__| | (_| | | | | | |  __/
  \_____|\__,_|\___||___/___/_|_| |_|\__, |  \_____|\__,_|_| |_| |_|\___|
                                      __/ |                              
                                     |___/                               """)

game_over = False
attempts = 0
number = random.randint(0, 100)
print(number)

print("Welcome to the guessing game!")
print("I'm thinking in a number between 0 and 100.")
difficult = input("Choose a difficult, type 'easy' or 'hard': ")
if difficult == "easy":
    attempts = 10
elif difficult == "hard":
    attempts = 5

while not game_over and attempts > 0:
    print(f"You have {attempts} attempts!")
    number_guessed = int(input("Make a guess: "))
    if number_guessed < number:
        print("Too low!")
        attempts -= 1
    elif number_guessed > number:
        print("too hight!")
        attempts -= 1
    elif number_guessed == number:
        print("Congratulations!\nis the correct number")
        game_over = True



