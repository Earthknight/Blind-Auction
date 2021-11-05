from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
bid_continue = True
bidders ={}
print(logo)
while bid_continue:
  name = input("Enter your name: ")
  value = input("How much you want ot bid: $")
  def add_Dict(name,value):
      bidders[name] = value
  def comp_bid(bidders):
      max_value =max(bidders)
      print(f"{max_value} won the bid")
      
  add_Dict(name,value)
  more = input("Are there any mor bidders if there then press Yes or else press No: ").lower()
  if more == 'yes':
    bid_continue = True
    clear()
  else:
    bid_continue = False
    comp_bid(bidders)
