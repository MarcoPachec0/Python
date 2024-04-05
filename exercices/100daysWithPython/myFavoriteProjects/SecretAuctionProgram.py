import replit
from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
participants = {}
bet_is_going = True
highest_bid = 0
winner = ""

def addParticipant(name, bet):
    participants[name] = bet

while bet_is_going:
    name = input("Please enter your name: ")
    bet = float(input("Please enter your bet: $"))
    addParticipant(name, bet)
    question = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if question == "no":
        bet_is_going = False
    elif question == "yes":
        et_is_going = True
        clear()

for name, bet in participants.items():
    if bet > highest_bid:
        highest_bid = bet
        winner = name

print(f"The winner is {winner} with a bid of ${highest_bid}")
