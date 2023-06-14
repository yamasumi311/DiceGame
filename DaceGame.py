import random

# Step1 in main program area - start game
number_dice = int(input('Enter number of dice: '))
ready = input('Ready to start? Hit any key to continue.')

dice_numbers = []


def roll_dice(n):
    for i in range(n):
        i = random.randint(1, 6)
        dice_numbers.append(i)
    return dice_numbers


userFirstRoll = roll_dice(n)
print(f'User first roll: {userFirstRoll}')

choice = input('Enter - to hold or r to roll again: ')

if not (choice == 'r'):
    dice_numbers = []
    print('Rolling again...')
    userNewRoll = roll_dice(n)
    print(f'User new roll: {userNewRoll}')

print('Computers turn')
dice_numbers = []
computerFirstRoll = roll_dice(n)
print(f'Computer first roll: {computerFirstRoll}')
print(f'Computer is thinking...')
print(f'')

