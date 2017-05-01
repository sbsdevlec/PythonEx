import turtle
import math
def hexagon(size):
    for _ in range(6):
        turtle.forward(size)
        turtle.left(60)

size=15
for _ in range (6):
    hexagon(size)
    turtle.forward(size)
    turtle.right(60)

turtle.exitonclick()