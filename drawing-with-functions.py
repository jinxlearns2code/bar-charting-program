# Bar charting program
import turtle

# Named constants
Y_TICK_MARKS = 6
STARTING_POINT = -200
TRACER_VALUE = 5
WINDOW_SIZE = 500
AXIS_LENGTH = 400

# Setup the environment and turtle
drawing_area = turtle.Screen()
turtle.setup(width=WINDOW_SIZE, height=WINDOW_SIZE)
turtle.hideturtle()
turtle.tracer(TRACER_VALUE)


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

# Draw ticks for y-axis
    total = 0
    turtle.pensize(width=3)
    turtle.penup()
    turtle.goto(STARTING_POINT, STARTING_POINT)
    turtle.pendown()
    for i in range(Y_TICK_MARKS):
        turtle.setheading(180)
        turtle.forward(8)
        turtle.penup()
        turtle.forward(14)
        turtle.setheading(270)
        turtle.forward(6)
        turtle.write(total, align='center', font=('Arial', 10, 'normal'))
        total = total + 6
        turtle.back(6)
        turtle.setheading(0)
        turtle.forward(22)
        turtle.setheading(90)
        turtle.forward(78)
        turtle.pendown()


# Draw bar chart/s using the data provided by the user (stored in 'arr' array)
def draw_bar_chart(h, colour):
    turtle.hideturtle()
    turtle.penup()
    turtle.fillcolor(colour)
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(gap)
    turtle.left(90)
    turtle.forward(h)
    turtle.write(str(display_number))
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(h)
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(gap)
    turtle.pendown()

    # Stop filling the shape
    turtle.end_fill()


# Prompt user for input - data points and individual data values
arr = []
value = int(turtle.numinput('Data Points', 'Please enter the total number of data points (0-20):', minval=0, maxval=20))
for num in range(value):
    array_item = int(turtle.numinput("Data Values", "Please enter data " + str(num + 1) + "'s" + " value (0-30):",
                                     minval=0, maxval=30))
    arr.append(array_item)

# Draw axes and ticks
axes()

# Define variables related to bar graph
color = ["pink", "aqua", "blanchedalmond", "coral", "lavender", "lightgreen", "darksalmon", "dodgerblue",
         "mediumorchid", "plum", "gold", "indianred", "palevioletred", "olive", "thistle", "tomato",
         "darkolivegreen", "sienna", "mediumpurple", "sandybrown"]
max_height = 30
turtle.penup()
turtle.goto(STARTING_POINT, STARTING_POINT + 1)


# Draw bar graph
for number in range(len(arr)):
    height = 390 / max_height * arr[number]
    width = 295 / value
    gap = 50 / value
    display_number = arr[number]
    draw_bar_chart(height, color[number])

# Program ends
turtle.done()
