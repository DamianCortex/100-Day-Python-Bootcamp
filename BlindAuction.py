
from turtle import clear
# Create empty Dictionary for name and price. 

BidEntry = {}

# Started condition of while loop which will be in motion equaling True.
bid_in_motion = True

# Made a function to find who's the highest bidder.
def whos_highestbidder(bidders):
    highestbid = 0
    winner = ""
    for bidder in bidders:
        bid_amount = bidders[bidder]
        if bid_amount > highestbid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The highest bid is in the amount of ${highest_bid} and the winner is {winner}")

# The while loop will have each bidder type in their name and price.
# Once the user has put in their name and price it will be added into the dictionary.
# The loop ends its condition and changes to false the moment the user enters done which will use the function above to caluclate winner and ends the problem. 

while bid_in_motion:
    name = input("What is your name? (If You're Done Type 'done')\n")
    if name == 'done':
        name.lower()
        print("Thank you we are done here.")
        whos_highestbidder(BidEntry)
        bid_in_motion = False
    elif not name.isalpha():
        print("You enter an invalid entry. Please show a Letter not a number.")
        continue
    else:
        price = float(input("Name your price:\n$"))
        BidEntry[name] = price
        clear()
    



