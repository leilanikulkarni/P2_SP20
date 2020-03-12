'''
Turtle Recursion (30pts)

1)  Using the turtle library, create the H fractal pattern as shown in the image (htree4.jpg) in this directory. (15pts)

2)  Using the turtle library, create any of the other recursive patterns in the directory. (10pts)

3)  Create your own work of art with a repeating pattern of your making.  It must be a repeated pattern using recursion.
Snowflakes, trees, and spirals are a common choice.  Or you can create a third one from the directory. (5pt)


 Each fractal should
 - be recursive
 - have a depth of at least 4
 - be contained on the screen

  Have fun!

'''

import turtle

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")

my_screen = turtle.Screen()
my_screen.bgcolor('white')

my_turtle.speed(0)  # setting up the turtle


def h_fractal(x, y, width, height, depth):  # recursive function
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.width(4)
        my_turtle.down()  # start drawing

        # draw top
        my_turtle.goto(x, y + height / 2)
        my_turtle.down()
        my_turtle.goto(x, y + height / 4)
        my_turtle.goto(x + width, y + height / 4)

        my_turtle.up()
        my_turtle.goto(x + width, y)
        my_turtle.down()
        my_turtle.goto(x + width, y + height / 2)
        my_turtle.goto(x + width, y + height / 4)  # positioning the first h

        h_fractal(x - width / 4, y + height / 2.6, width / 2, height / 2, depth - 1)
        h_fractal(x + width * (3 / 4), y + height / 2.6, width / 2, height / 2, depth - 1)
        h_fractal(x - width / 4, y - height / 6.7, width / 2, height / 2, depth - 1)
        h_fractal(x + width * (3 / 4), y - height / 6.7, width / 2, height / 2, depth - 1)  # setting up the recursive
        # smaller shapes


h_fractal(-150, -100, 320, 550, 4)  # creates a repeating h pattern

my_screen.clear()
my_turtle.home()  # clearing the screen and returning the turtle to its original position


def plus_fractal(x, y, width, height, depth):  # setting up recursive function
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.width(4)
        my_turtle.down()  # start drawing

        my_turtle.goto(x, y + height / 2)
        my_turtle.up()
        my_turtle.goto(x, y + height / 4)

        my_turtle.down()
        my_turtle.goto(x + width / 2, y + height / 4)
        my_turtle.goto(x - width / 2, y + height / 4)  # drawing the first plus sign

        plus_fractal(x - width / 2, y + height / 8, width / 2, height / 2, depth - 1)
        plus_fractal(x + width / 2, y + height / 8, width / 2, height / 2, depth - 1)
        plus_fractal(x, y - height / 8, width / 2, height / 2, depth - 1)
        plus_fractal(x, y + height / 2.5, width / 2, height / 2, depth - 1)  # drawing the recursive smaller plus signs


plus_fractal(0, -130, 350, 600, 4)  # creates a repeating plus sign shape

my_screen.clear()
my_turtle.home()  # clearing the screen and returning the turtle home


def snowflake_fractal(x, y, width, height, depth):  # recursive function
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.width(0)
        my_turtle.down()  # start drawing

        my_turtle.goto(x + width, y)
        my_turtle.goto(x - width, y)

        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x + width / 1.5, y + height)
        my_turtle.goto(x - width / 1.5, y - height)

        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x + width / 1.5, y - height)
        my_turtle.goto(x - width / 1.5, y + height)  # drawing the first part of the snowflake

        snowflake_fractal(x - width / 1.2, y, width / 3, height / 3, depth - 1)
        snowflake_fractal(x + width / 1.2, y, width / 3, height / 3, depth - 1)
        snowflake_fractal(x + width / 2.1, y + height / 1.4, width / 3, height / 3, depth - 1)
        snowflake_fractal(x - width / 2.1, y + height / 1.4, width / 3, height / 3, depth - 1)
        snowflake_fractal(x + width / 2.1, y - height / 1.4, width / 3, height / 3, depth - 1)
        snowflake_fractal(x - width / 2.1, y - height / 1.4, width / 3, height / 3, depth - 1)  # drawing the recursive
        # smaller x like shapes to the snowflake


snowflake_fractal(10, 10, 250, 300, 4)  # creates a snowflake


my_screen.exitonclick()  # screen exits when you click on it
