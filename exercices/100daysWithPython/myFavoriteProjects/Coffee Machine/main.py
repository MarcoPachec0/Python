is_running = True
from menu import resources, menu

money = 0
coins = [0.25, 0.10, 0.05, 0.01]


def make_drink(drink_name):
    ingredients = menu[drink_name]["ingredients"]
    for ingredient, quantity in ingredients.items():
        if resources[ingredient] < quantity:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    for ingredient, quantity in ingredients.items():
        resources[ingredient] -= quantity
    return True


while is_running:
    option = int(input("What would you like?\nEspresso: 1\nLatte: 2\nCappuccino: 3\nPress 0 to turn off the machine"))
    print("----------------------------------")
    if option == 0:
        is_running = False

    elif option == 123:
        print("Remaining ingredients:")
        for item, quantity in resources.items():
            print(f"{item}: {quantity}")
        print("----------------------------------")

    elif option in [1, 2, 3]:
        drink_name = ["espresso", "latte", "cappuccino"][option - 1]
        drink_cost = menu[drink_name]["cost"]

        print(f"The cost of {drink_name} is ${drink_cost}. Please insert coins.")
        total_inserted = 0
        for coin in coins:
            num_coins = int(input(f"Insert {coin} coins: "))
            total_inserted += num_coins * coin

        if total_inserted >= drink_cost:
            change = total_inserted - drink_cost
            if make_drink(drink_name):
                print(f"Here is your {drink_name}. Enjoy! Your change is ${change:.2f}.")
                money += drink_cost
        else:
            print("Sorry, that's not enough money. Money refunded.")
