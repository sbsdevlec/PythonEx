import turtle
import math
def draw_shape(sides, length, dir):
    for _ in range(sides):
        turtle.forward(length)
        turtle.right(dir * 360 / sides)

for sides in range(3,10):
    draw_shape(sides,50,1)

for sides in range(3,10):
    draw_shape(sides,50,-1)


turtle.exitonclick()