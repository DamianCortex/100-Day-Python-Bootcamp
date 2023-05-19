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

while True:
  coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
  coffee_type = coffee_type.lower()
  report = resources
  money_amount = ""
  if coffee_type == 'espresso':
    espresso_water = MENU["espresso"]["ingredients"]["water"]
    espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
    print("Current Report for Coffee Machine Resources:\n")
    print(report)
    
    if espresso_coffee <= resources["coffee"] and espresso_water <= resources["water"]:
      resources["water"] -= espresso_water
      resources["coffee"] -= espresso_coffee
      money_owed = MENU["espresso"]["cost"]
    else:
      print("We do not have the resources for this drink.")
      
    while True:
      print("You owe $" + str(round(abs(money_owed), 2)) + "\n")
      coins = input("Please Insert Coins (Choose Quarter, Dime, or Nickle) If you're out of money, press 'n' for no more coins:")
      coins.lower()
      if coins == 'quarter':
        money_amount += coins
        money_owed -= .25
        if money_owed == 0:
          print("\nUpdated Coffee Machine Resources: \n")
          print(report)
          print("\nEnjoy your espresso!\n")
          break
        elif money_owed < 0:
          print("Oh and here's your change!", round(abs(money_owed), 2))
          break
        else:
          continue
      elif coins == 'dime':
        money_amount += coins
        money_owed -= .10
        if money_owed == 0:
          print("\nUpdated Coffee Machine Resources: \n")
          print(report)
          print("\nEnjoy your espresso!\n")
          break
        elif money_owed < 0:
          print("Oh and here's your change!", round(abs(money_owed), 2))
          print("\nUpdated Coffee Machine Resources: \n")
          print(report)
          print("\nEnjoy your espresso!\n")
          break
        else:
          continue
      elif coins == 'nickle':
        money_amount += coins
        money_owed -= .05
        if money_owed == 0:
          print("\nUpdated Coffee Machine Resources: \n")
          print(report)
          print("\nEnjoy your espresso!\n")
          break
        elif money_owed < 0:
          print("Oh and here's your change!", round(abs(money_owed), 2))
          print("\nUpdated Coffee Machine Resources: \n")
          print(report)
          print("\nEnjoy your espresso!\n")
          break
        else:
          continue
      elif coins == 'n':
        print("You have no more coins. Here's your refund")
        money_owed = MENU["espresso"]["cost"]
        break
      else:
        print("Invalid Entry. Try again")
    
  elif coffee_type == 'latte':
    latte_water = MENU["latte"]["ingredients"]["water"]
    latte_milk = MENU["latte"]["ingredients"]["milk"]
    latte_coffee = MENU["latte"]["ingredients"]["coffee"]
    money_owed = MENU["latte"]["cost"]
    print("Current Report for Coffee Machine Resources:\n")
    print(report)
    if latte_water <= resources["water"] and latte_milk <= resources["milk"] and latte_coffee <= resources["coffee"]:
      resources["water"] -= latte_water
      resources["milk"] -= latte_milk
      resources["coffee"] -= latte_coffee
    else:
      print("We do not have the resources for this drink.")

    while True:
      print("You owe $" + str(round(abs(money_owed), 2)) + "\n")
      coins = input("Please Insert Coins (Choose Quarter, Dime, or Nickle) If you're out of money, press 'n' for no more coins:")
      coins.lower()
      if coins == 'quarter':
        money_amount += coins
        money_owed -= .25
        if money_owed == 0:
          print("\nUpdated Coffee Machine Resources: \n")
          print(report)
          print("\nEnjoy your latte!\n")
          break
        elif money_owed < 0:
          print("Oh and here's your change!", round(abs(money_owed), 2))
          print("\nUpdated Coffee Machine Resources: \n")
          print(report)
          print("\nEnjoy your latte!\n")
          break
        else:
          continue
      elif coins == 'dime':
        money_amount += coins
        money_owed -= .10
        if money_owed == 0:
          print("\nUpdated Coffee Machine Resources: \n")
          print(report)
          print("\nEnjoy your latte!\n")
          break
        elif money_owed < 0:
          print("Oh and here's your change!", round(abs(money_owed), 2))
          print("\nUpdated Coffee Machine Resources: \n")
          print(report)
          print("\nEnjoy your latte!\n")
          break
        else:
          continue
      elif coins == 'nickle':
        money_amount += coins
        money_owed -= .05
        if money_owed == 0:
          print("\nUpdated Coffee Machine Resources: \n")
          print(report)
          print("\nEnjoy your latte!\n")
          break
        elif money_owed < 0:
          print("Oh and here's your change!", round(abs(money_owed), 2))
          print("\nUpdated Coffee Machine Resources: \n")
          print(report)
          print("\nEnjoy your latte!\n")
          break
        else:
          continue
      elif coins == 'n':
        print("You have no more coins. Here's your refund")
        money_owed = MENU["latte"]["cost"]
        break
      else:
        print("Invalid Entry. Try again")
        
  elif coffee_type == 'cappuccino':
    cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
    cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
    cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
    money_owed = MENU["cappuccino"]["cost"] 
    print("Current Report for Coffee Machine Resources:\n")
    print(report)
    if cappuccino_water <= resources["water"] and cappuccino_milk <= resources["milk"] and cappuccino_coffee <= resources["coffee"]:
      resources["water"] -= cappuccino_water
      resources["milk"] -= cappuccino_milk
      resources["coffee"] -= cappuccino_coffee
    else:
      print("We do not have the resources for this drink.")

    while True:
      print("You owe $" + str(round(abs(money_owed), 2)) + "\n")
      coins = input("Please Insert Coins (Choose Quarter, Dime, or Nickle) If you're out of money, press 'n' for no more coins:")
      coins.lower()
      if coins == 'quarter':
        money_amount += coins
        money_owed -= .25
        if money_owed == 0:
          print("\nUpdated Coffee Machine Resources: \n")
          print(report)
          print("\nEnjoy your cappuccino!\n")
          break
        elif money_owed < 0:
          print("Oh and here's your change!", round(abs(money_owed), 2))
          print("\nUpdated Coffee Machine Resources: \n")
          print(report)
          print("\nEnjoy your cappuccino!\n")
          break
        else:
          continue
      elif coins == 'dime':
        money_amount += coins
        money_owed -= .10
        if money_owed == 0:
          print("\nUpdated Coffee Machine Resources: \n")
          print(report)
          print("\nEnjoy your cappuccino!\n")
          break
        elif money_owed < 0:
          print("Oh and here's your change!", round(abs(money_owed), 2))
          print("\nUpdated Coffee Machine Resources: \n")
          print(report)
          print("\nEnjoy your cappuccino!\n")
          break
        else:
          continue
        
      elif coins == 'nickle':
        money_amount += coins
        money_owed -= .05
        if money_owed == 0:
          print("\nUpdated Coffee Machine Resources: \n")
          print(report)
          print("\nEnjoy your cappuccino!\n")
          break
        elif money_owed < 0:
          print("Oh and here's your change!", round(abs(money_owed), 2))
          print("\nUpdated Coffee Machine Resources: \n")
          print(report)
          print("\nEnjoy your cappuccino!\n")
          break
        else:
          continue
      elif coins == 'n':
        print("You have no more coins. Here's your refund")
        money_owed = MENU["cappuccino"]["cost"]
        break
      else:
        print("Invalid Entry. Try again")
    
  elif coffee_type == 'off':
    print("Coffee machine: OFF Ready for maintenance")
    print(report)
  else:
    print("You made an invalid entry\n")

