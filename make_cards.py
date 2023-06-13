suits = ['Clubs', 'Hearts', 'Diamonds', 'Spades']
cardno = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def make_cards():
    cards = []  # start with empty list and add cards
    for s in suits:
        for i in cardno:
            cards.append(f'{i} - {s}')
    return cards

my_cards = make_cards()
print(my_cards)