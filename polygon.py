import turtle

# Create a screen object and set background color

screen = turtle.Screen()

screen.bgcolor("lime")

screen.setup(400, 400)

# Create a turtle object

polygon = turtle.Turtle()

# Polygon properties

num_sides = 6

side_length = 70

angle = 360.0 / num_sides

# Draw the polygon

for i in range(num_sides):

    polygon.forward(side_length)

    polygon.right(angle)

turtle.done()