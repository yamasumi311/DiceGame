# my functions

import turtle

shelly = turtle.Turtle()


# square function creates square of size 100
def square(s):
    for i in range(4):
        shelly.forward(s)  # each side of square is 100
        shelly.left(90)


for i in range(25):
    square(i)
    shelly.forward(i)