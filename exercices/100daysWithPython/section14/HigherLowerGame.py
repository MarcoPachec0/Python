import random
from replit import clear
from art import logo, vs
from game_data import data

def get_random_accounts():
    account_a = random.choice(data)
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    return account_a, account_b

def format_account(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_guess(guess, a_followers, b_followers):
    return (guess == "a" and a_followers > b_followers) or (guess == "b" and b_followers > a_followers)

def game():
    print(logo)
    score = 0
    game_over = False

    while not game_over:
        account_a, account_b = get_random_accounts()

        print(f"Compare A: {format_account(account_a)}.")
        print(vs)
        print(f"Against B: {format_account(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_followers = account_a["follower_count"]
        b_followers = account_b["follower_count"]
        is_correct = check_guess(guess, a_followers, b_followers)

        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_over = True
            print(f"Sorry, that's wrong. Final score: {score}.")

game()
