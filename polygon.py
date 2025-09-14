import turtle

# Create a screen object and set background color

screen = turtle.Screen()

screen.bgcolor("lime")

screen.setup(400, 400)

# Create a turtle object

square = turtle.Turtle()

# Polygon properties

num_sides = 4

side_length = 180

angle = 360.0 / num_sides

# Draw the polygon

for i in range(num_sides):

    square.forward(side_length)

    square.right(angle)

turtle.done()