from replit import clear
from art import logo

def greaterBid(bids_dict):
  greater_bid = 0
  for bidder in bids_dict:
    bid_amount = all_bids[bidder]
    if bid_amount > greater_bid:
      greater_bid = bid_amount
      winner = bidder
  print(f'The winner is {winner} with a bid of ${greater_bid}.')

print(logo)
all_bids = {}
event_continues = True

while event_continues:
  
  bidder = input("What's your name? ")
  bid_value = int(input("What's your bid? $"))
  
  all_bids[bidder] = bid_value
  
  should_continue = input("Are there any other bidders? Type   'yes' or 'no'.\n")

  if should_continue == 'no':
    event_continues = False
  else:
    clear()

greaterBid(all_bids)