# Importing Random Module
import random

# Asking player for name, welcoming player, and starting player out with $200
player_name = input("What is your name?\n")
print(f"Greetings {player_name}, Welcome to Blackjack\n\n")
money_amount = 200


# Starting gameloop to loop from the cards on the deck to be reset every round.
gameloop = True
while gameloop:
  cards_on_deck = {
                 "Ace Diamond": 11, "Diamond 1": 1, "Diamond 2": 2, "Diamond 3":3, 
                 "Diamond 4" : 4, "Diamond 5": 5, "Diamond 6" : 6, 
                 "Diamond 7": 7, "Diamond 8":8, "Diamond 9":9, 
                 "Diamond 10": 10, "Diamond Jack":10, "Diamond Queen": 10, 
                 "Diamond King":10,
                 "Ace Hearts": 11, "Hearts 1": 1, "Hearts 2": 2, "Hearts 3": 3, 
                 "Hearts 4" : 4, "Hearts 5": 5, "Hearts 6" : 6, "Hearts 7": 7, 
                 "Hearts 8":8, "Hearts 9":9, "Hearts 10": 10, "Hearts Jack":10, 
                 "Hearts Queen": 10, "Hearts King":10,
                 "Ace Spades": 11, "Spades 1": 1, "Spades 2": 2, "Spades 3": 3, 
                 "Spades 4" : 4, "Spades 5": 5, "Spades 6" : 6, "Spades 7": 7, 
                 "Spades 8":8, "Spades 9":9, "Spades 10": 10, "Spades Jack":10, 
                 "Spades Queen": 10, 
                 "Spades King":10,
                 "Ace Clubs": 11, "Clubs 1": 1, "Clubs 2": 2, "Clubs 3": 3, 
                 "Clubs 4" : 4, "Clubs 5": 5, "Clubs 6" : 6, "Clubs 7": 7, 
                 "Clubs 8":8, "Clubs 9":9, "Clubs 10": 10, "Clubs Jack":10, 
                 "Clubs Queen": 10, 
                 "Clubs King":10
                  }

  # Starting player with an empty hand, starting dealer with the illusion of an empty card flipped around, and displaying money amount player currently has. 
  player_cards = {}
  dealer_cards = {"Hidden Card":0}  
  print(f"{player_name} amount: ${money_amount}\n")

  # Starting small loop to make sure player enters an integer amount for the amount they want to bet and make sure they don't try to bet over the amount of money they already have.
  while True:
    bet_amount = input("How much money would you like to bet? Place your bet: \n")
    if not bet_amount.isdigit():
      print("Invalid Entry... like... you know try a number.\n")
    elif not bet_amount.isdigit or int(bet_amount) > money_amount:
      print("Pal, you can't bet over the amount of money you have and chances are you also didn't use a number. Try again.\n")
    else:
      bet_amount = int(bet_amount)
      break
  print(f"You bet ${bet_amount}!\n")

  # Player and Dealer both draw their first cards
  print("Player's Hand:")
  chosen_card = random.choice(list(cards_on_deck.keys()))
  if len(cards_on_deck) == 0:
    print("We have no more cards!")
  player_cards[chosen_card] = cards_on_deck[chosen_card]
  del cards_on_deck[chosen_card]
  print(player_cards)
  print("\nDealer's Hand:")
  chosen_card = random.choice(list(cards_on_deck.keys()))
  if len(cards_on_deck) == 0:
    print("We have no more cards!")
  dealer_cards[chosen_card] = cards_on_deck[chosen_card]
  del cards_on_deck[chosen_card]
  print(dealer_cards)

  # The decision loop asks if the player wants to draw another card or not.
  yes_no_loop = True
  while yes_no_loop:
    yes_no = input("\nWould you like to draw another card? (y/n)\n\n")
    yes_no = yes_no.lower()
    if yes_no == "y" or yes_no == "yes":

      # We player says yes and here we take a random card from the deck and put it in the player's hand. 
      print("Player's Hand:")
      chosen_card = random.choice(list(cards_on_deck.keys()))
      player_cards[chosen_card] = cards_on_deck[chosen_card]
      sum_of_player_cards = sum(player_cards.values())

      # Here we see if the card is an Ace and if that Ace which is defaulted to an 11 goes over 21 in which the player decides if that Ace is an 11 or 1. 
      if chosen_card.startswith("Ace") and sum_of_player_cards > 21:
        new_value = input("You went above 21,but because you drew an Ace. Would you like to count it as 1 or 11?\n")
        while new_value not in ["1", "11"]:
          new_value = input("Invalid choice. Please enter 1 or 11.\n")
        if new_value == "1":
          player_cards[chosen_card] = 1
        else:
          player_cards[chosen_card] = 11 
      
      if len(cards_on_deck) == 0:
        print("We have no more cards!")
      del cards_on_deck[chosen_card]
      print(player_cards)
      sum_of_player_cards = sum(player_cards.values())
      
      """
      Just to test to make sure sum_of_player_cards is working.
      print("This is a test:")
      print(sum_of_player_cards)
      """
      
      print("Dealer's Hand:")
      sum_of_dealer_cards = sum(dealer_cards.values())
      print(dealer_cards)
      
      """
      Just to test to make sure sum_of_dealer_cards is working.
      print("This is a test")
      print(sum_of_dealer_cards)
      """

      # If player just goes over 21 the player loses the amount of money he bet.
      if sum_of_player_cards > 21:
        money_amount = money_amount - int(bet_amount)
        print(f"Bust! You lost ${bet_amount} and now have ${money_amount}\n\n")
        print("Next Round")
        yes_no_loop = False

      # However if player equals to 21 player wins twice the amount of the bet money amount.
      elif sum_of_player_cards == 21:
        double_bet_win = int(bet_amount) + int(bet_amount)
        money_amount = money_amount + double_bet_win
        print(f"You won ${double_bet_win} this round automatically by scoring a perfect 21.\nYou now have a total of {money_amount} ")  
      else:
        continue

    # Player chooses no. He will run into two scenarios. Right now the hidden card of the dealer is "flipped around" (Actually dels the hidden card and replaces with a random card from the deck.)
    elif yes_no == "n" or yes_no == 'no':
      print("Player's Hand:")
      print(player_cards)
      print("\nDealer's Hand:")
      chosen_card = random.choice(list(cards_on_deck.keys()))
      del dealer_cards["Hidden Card"]
      if len(cards_on_deck) == 0:
        print("We have no more cards!")
      dealer_cards[chosen_card] = cards_on_deck[chosen_card]
      print(dealer_cards)
      
      sum_of_player_cards = sum(player_cards.values())
      sum_of_dealer_cards = sum(dealer_cards.values())

      # If the player's total sum amount is below 16 he has to draw another card. 
      if sum_of_player_cards <= 16:
        print(f"{player_name} is at or below 16 in total sum of cards and must pick up another one.")
        Enter_to_Proceed = input("Press 'Enter' to continue")
        chosen_card = random.choice(list(cards_on_deck.keys()))
        if len(cards_on_deck) == 0:
          print("We have no more cards!")
        player_cards[chosen_card] = cards_on_deck[chosen_card]
        del cards_on_deck[chosen_card]
        print("Player's Hand:")
        print(player_cards)
        sum_of_player_cards = sum(player_cards.values())

        # Dealer draws final card
        print("Dealer will now draw its final card.\n")
        Enter_to_Proceed = input("Press 'Enter' to continue")
        chosen_card = random.choice(list(cards_on_deck.keys()))
        if len(cards_on_deck) == 0:
          print("We have no more cards!")
        dealer_cards[chosen_card] = cards_on_deck[chosen_card]
        print("\nDealer's Hand:")
        print(dealer_cards)
      
      # If player has the sum of cards over 16. Then we proceed to make the final comparison between player and dealer card sums.  
      elif sum_of_player_cards > 16:
        print("Dealer will now draw its final card.\n")
        Enter_to_Proceed = input("Press 'Enter' to continue")
        chosen_card = random.choice(list(cards_on_deck.keys()))
        if len(cards_on_deck) == 0:
          print("We have no more cards!")
        dealer_cards[chosen_card] = cards_on_deck[chosen_card]
        print("\nDealer's Hand:")
        print(dealer_cards)
        
      sum_of_player_cards = sum(player_cards.values())
      sum_of_dealer_cards = sum(dealer_cards.values())

      # Here we determine the winner player or dealer
      if sum_of_player_cards > sum_of_dealer_cards:
        double_bet_win = int(bet_amount) + int(bet_amount)
        money_amount = money_amount + double_bet_win
        print(f"{player_name} wins ${double_bet_win} and has a total of ${money_amount}")
      elif sum_of_dealer_cards > sum_of_player_cards:
        money_amount = money_amount - bet_amount
        print(f"Dealer wins you lose ${bet_amount} which leaves you with ${money_amount}")
      else:
        print(f"This is a Draw. You win nothing, you lose nothing. You are current at ${money_amount}.")
      # test
      break
    else:
      print("You entered an invalid choice. Try Again")

  # This last area shows that if the player runs out of money. The gameloop breaks and it's Game over. 
  if money_amount <= 0:
    print("You are broke! Game Over!")
    gameloop = False
  else:
    gameloop = True
    
  