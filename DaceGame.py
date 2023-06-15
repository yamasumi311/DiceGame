import random
import time

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
def find_winner(cdice_list, udice_list):
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


def get_user_choices():
    # get user choices
    user_choices = input('Enter - to hold or r to roll again: ')
    # check length of user input
    while len(user_choices) != number_dice:
        print(f'You must enter {number_dice} choices.')
        user_choices = input('Enter - to hold or r to roll again: ')
    return user_choices


# roll again function
def roll_again(choices, dice_list):
    print('Rolling again...')
    for i in range(len(choices)):
        if choices[i] == 'r':
            dice_list[i] = random.randint(1, 6)
    time.sleep(3)


# take a turn: choose - roll - result
def take_turn():
    userChoices = get_user_choices()
    # step5 - roll again based on user choices
    roll_again(userChoices, user_rolls)
    print(f'Player new roll: {user_rolls}')


take_turn()

# computer's turn
print('Computer is thinking...')
time.sleep(3)


def computer_strategy1(n):
    # create computer choices: roll everything again
    choices = '' # start with an empty list of choices
    for i in range(n):
        choices = choices + 'r'
    return choices


def computer_strategy2(n):
    # create computer choices: roll if < 5
    choices = ''  # start with an empty list of choices
    for i in range(n):
        if computer_rolls[i] < 5:
            choices = choices + 'r'
        else:
            choices = choices + '-'
    return choices


# step6
def computers_turn():
    # decide on what choice - using one of the strategy functions
    computer_choices = computer_strategy2(number_dice)
    print(f'Computer Choice: {computer_choices}')
    # Computer rolls again using the choices it made
    roll_again(computer_choices, computer_rolls)
    print(f'Computer new roll: {computer_rolls}')


computers_turn()


# allow roll again
def another_chance():
    answer = input('Do you want to roll again?(y or n): ')
    while answer == 'y' or answer == 'n':
        return answer
    else:
        print('invalid input. Try again')
        answer = input('Do you want to roll again?(y or n): ')
        return answer


# user to decide if they want another rolls
anotherChance = another_chance()


def roll_or_not(anotherChance):
    if anotherChance == 'y':
        return take_turn()


# another roll depending on user's choice
roll_or_not(anotherChance)

# computer's turn
computers_turn()


# final line in code - deciding who wins
find_winner(computer_rolls, user_rolls)


