import turtle
import math

wn = turtle.Screen()
wn.bgcolor("lightgreen")
turtle.shape("turtle")
turtle.color("blue")

turtle.penup()                # This is new
size = 20
for i in range(30):
   turtle.stamp()             # Leave an impression on the canvas
   size = size + 3          # Increase the size on every iteration
   turtle.forward(size)       # Move tess along
   turtle.right(24)           #  ...  and turn her



turtle.exitonclick()