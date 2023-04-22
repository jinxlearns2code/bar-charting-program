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
    turtle.done()


main()
