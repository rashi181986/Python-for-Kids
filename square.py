# Draw a square using Turtle

import turtle

t = turtle.Turtle()

for i in range(4):
    t.forward(100)  # Move forward 100 pixels
    t.right(90)     # Turn right by 90 degrees

turtle.done()