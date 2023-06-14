import random

# Step1 in main program area - start game
number_dice = int(input('Enter number of dice: '))
ready = input('Ready to start? Hit any key to continue.')


# rolling dice function
def roll_dice(n):
    dice = []  # start with empty list of dice
    # add random numbers between 1 to 6 to the list
    for i in range(n):
        dice.append(random.randint(1, 6))
    return dice


# step2 in main program area - roll dice
# user turn to roll
user_rolls = roll_dice(number_dice)
print(f'User first roll: {user_rolls}')
# computer's turn to roll
print('Computers turn')
computer_rolls = roll_dice(number_dice)
print(f'Computer first roll: {computer_rolls}')

# step3 find winner function
def find_winner(cdice_list, udice_list)
    computer_total = sum(cdice_list)
    user_total = sum(udice_list)
    print(f'Computer total: {computer_total}')
    print(f'User total: {user_total}')
    if user_total > computer_total:
        print('User wins!')
    elif user_total < computer_total:
        print('Computer wins!')
    else:
        print('It is a tie!')




print(f'Computer is thinking...')
print(f'')


choice = input('Enter - to hold or r to roll again: ')

if not (choice == 'r'):
    dice_numbers = []
    print('Rolling again...')
    userNewRoll = roll_dice(n)
    print(f'User new roll: {userNewRoll}')


