MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

def display_report():
    print("Current Report for Coffee Machine Resources:\n")
    print(resources)

def check_resources(drink):
    drink_ingredients = MENU[drink]["ingredients"]
    for ingredient, amount in drink_ingredients.items():
        if resources[ingredient] < amount:
            return False
    return True

def update_resources(drink):
    drink_ingredients = MENU[drink]["ingredients"]
    for ingredient, amount in drink_ingredients.items():
        resources[ingredient] -= amount

def process_coins(cost):
    money_owed = cost
    money_amount = ""
    while money_owed > 0:
        print("You owe $" + str(round(abs(money_owed), 2)) + "\n")
        coins = input("Please Insert Coins (Choose 'Q' for Quarter, 'D' for Dime, or 'N' for Nickel). If you're out of money, press 'N' for no more coins: ").lower()
        if coins == 'Quarter' or 'Q':
            money_amount += coins
            money_owed -= 0.25
        elif coins == 'Dime' or 'D':
            money_amount += coins
            money_owed -= 0.10
        elif coins == 'Nickel' or 'N':
            money_amount += coins
            money_owed -= 0.05
        elif coins == 'n':
            print("You have no more coins. Here's your refund.")
            money_owed = cost
            break
        else:
            print("Invalid entry. Try again.")
    if money_owed < 0:
        print("Oh and here's your change!\n", round(abs(money_owed), 2))
    return money_owed, money_amount

def make_coffee(drink):
    if check_resources(drink):
        update_resources(drink)
        cost = MENU[drink]["cost"]
        money_owed, money_amount = process_coins(cost)
        if money_owed == 0:
            print("\nUpdated Coffee Machine Resources: \n")
            display_report()
            print("\nEnjoy your", drink + "!\n")
        else:
            print("\nEnjoy your", drink + "!\n")
            print("\nBut don't forget your change!.")
    else:
        print("We do not have the resources for this drink.")

while True:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if coffee_type == 'off':
        print("Coffee machine: OFF. Ready for maintenance.")
        display_report()
        break
    elif coffee_type in ['espresso', 'latte', 'cappuccino']:
        make_coffee(coffee_type)
    else:
        print("You made an invalid entry.\n")
