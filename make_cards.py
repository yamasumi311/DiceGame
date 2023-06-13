import random

suits = ['Clubs', 'Hearts', 'Diamonds', 'Spades']
cardno = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


def make_card():
    s = random.choice(suits)
    n = random.choice(cardno)
    card = f'{s} - {n}'
    return card


numberOfCard = int(input('How many cards do you want to select?: '))
i = 0
while i < numberOfCard:
    my_card = make_card()
    print(my_card)
    i += 1
