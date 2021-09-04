from art import logo
import os
def clear(): return os.system('clear')


print(logo)
print('Welcome to the secret auction program.')

bids = {}
more_entries = True


def check_winner():
    highest_bid = 0
    winner = ''
    for bidder in bids:
        if bids[bidder] > highest_bid:
            highest_bid = bids[bidder]
            winner = bidder
    print(f'{winner} won the auction with a bid of ${highest_bid}!')


while more_entries:
    name = input('What is your name?: ')
    bid = int(input('What\'s your bid?: '))
    bids[name] = bid
    more_users = input("Are there any other bidders? type 'yes' or 'no'")
    if more_users == 'no':
        check_winner()
        more_entries = False
    else:
        clear()
