import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_over = False
rival_points = 0
player_points = 0

def remove_card(cards, card_to_remove):
    cards.remove(card_to_remove)

def add_card():
    card = random.choice(cards)
    remove_card(cards, card)
    return card

while not game_over:
    rival_points += add_card()
    player_points += add_card()
    print(f"Rival Points: {rival_points}")
    print(f"Your Points: {player_points}")

    if player_points >= 21 or rival_points >= 21:
        game_over = True
        continue

    choice = input("Another card? (y/n): ")

    if choice.lower() == "n":
        game_over = True

if rival_points > 21 and player_points <= 21:
    print(f"Rival busted with {rival_points} points. You win!")
elif player_points > 21 and rival_points <= 21:
    print(f"You busted with {player_points} points. You lose!")
elif player_points > 21 and rival_points > 21:
    print("Both busted! It's a tie.")
else:
    if rival_points > player_points:
        print(f"You lose!\nYour Points: {player_points}\nRival points: {rival_points}")
    elif player_points > rival_points:
        print(f"You win!\nYour Points: {player_points}\nRival points: {rival_points}")
    else:
        print("It's a tie!")
