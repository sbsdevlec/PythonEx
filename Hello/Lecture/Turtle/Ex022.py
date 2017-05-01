import turtle
import math

wn = turtle.Screen()  # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Tess & Alex")

tess = turtle.Turtle()  # Create tess and set some attributes
tess.color("hotpink")
tess.pensize(5)

tess.forward(80)  # Make tess draw equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)  # Complete the triangle


turtle.exitonclick()