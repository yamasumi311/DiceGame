# my functions

import turtle

shelly = turtle.Turtle()


# square function creates square of size 100
def square():
    for i in range(4):
        shelly.forward(100)  # each side of square is 100
        shelly.left(90)


square()  # calling the function
shelly.forward(100)  # move forward
square()  # make another square by calling the function
shelly.forward(100)  # move forward
square()  # make another square by calling the function again
