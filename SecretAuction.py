print("Welcome to secret auction!")

def find_highest_bidder(auctions):
    highest_bidder = ""
    highest_bid_amount = 0
    for bidder in auctions:
        amount = auctions[bidder]
        if amount > highest_bid_amount:
            highest_bidder = bidder
            highest_bid_amount = amount

    print(f"The winner is {highest_bidder} with ${highest_bid_amount}")

more_players = True
auctions = {}
while more_players:
    name = input("What is your name? : ")
    bid_amount = int(input("what is your bid amount? : $ "))
    auctions[name] = bid_amount

    want_to_continue = input("Is there any other player? : y - yes, n - no : ").lower()
    if want_to_continue == "n":
        more_players = False

find_highest_bidder(auctions)





