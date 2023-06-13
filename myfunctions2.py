# my functions

import turtle

shelly = turtle.Turtle()


# square function creates square of size 100
def square(s):
    for i in range(4):
        shelly.forward(s)  # each side of square is 100
        shelly.left(90)


square(100)  # calling the function
shelly.forward(100)  # move forward
square(200)  # make another square by calling the function
shelly.forward(100)  # move forward
square(300)  # make another square by calling the function again