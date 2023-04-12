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

bids = {}
continuar = True

def find_highest_bid(bid):
    winner = ''
    highest_bid = 0
    
    for i in bids:
        if bids[i] > highest_bid:
            winner == i
            highest_bid == bid[i]
    print(f'The winner is {i} with a bid of ${bids[i]}')
    
while continuar is True:
    name = input('Type your name: ')
    price = float(input('Type your bid: $'))
    bids[name] = price
    should_continue = input('Are there any other bidders? Type y or n: ')
    if should_continue == 'n':
        continuar = False
        find_highest_bid(bids)
    