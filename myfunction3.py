# functions that return values
# define a function that finds average of a list
def average(myList):
    total = sum(myList)  # use the sum function in python lists
    average = total / len(myList)  # len gives number of items
    return average


# use the function
scores = []

choice = input('Enter return to start adding scores! ').lower()
while not (choice == 'c'):
    score = int(input('Enter score: '))
    scores.append(score)
    choice = input('Enter return to continue adding scores or c to calculate the average score: ').lower()

averageScore = average(scores)
print(f'The average of the scores is {averageScore}.')
