# Bar charting program
import turtle

# Named constants
Y_TICK_MARKS = 6
STARTING_POINT = -200
ANIMATION_SPEED = 0
WINDOW_SIZE = 500
AXIS_LENGTH = 400

# Setup the environment and turtle
drawing_area = turtle.Screen()
drawing_area.setup(width=WINDOW_SIZE, height=WINDOW_SIZE)
turtle.speed(ANIMATION_SPEED)
turtle.hideturtle()


# Main function
def main():
    axes()
    ticks()


# Function to draw axes
def axes():
    turtle.pensize(width=3)
    turtle.penup()
    turtle.goto(STARTING_POINT, STARTING_POINT)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(400)
    turtle.stamp()
    turtle.right(180)
    turtle.penup()
    turtle.goto(STARTING_POINT, STARTING_POINT)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(400)
    turtle.stamp()
    turtle.right(180)


# Function to draw tick marks for y-axis
def ticks():
    total = 0
    turtle.pensize(width=3)
    turtle.penup()
    turtle.goto(STARTING_POINT, STARTING_POINT)
    turtle.pendown()
    for i in range(Y_TICK_MARKS-1):
        turtle.setheading(180)
        turtle.forward(8)
        turtle.penup()
        turtle.forward(14)
        turtle.setheading(270)
        turtle.forward(6)
        turtle.write(total)
        total = total + 6
        turtle.back(6)
        turtle.setheading(0)
        turtle.forward(22)
        turtle.pendown()
        turtle.setheading(90)
        turtle.forward(78)
    turtle.penup()
    turtle.setheading(180)
    turtle.forward(22)
    turtle.setheading(270)
    turtle.forward(6)
    turtle.write(30)
    turtle.done()


main()
