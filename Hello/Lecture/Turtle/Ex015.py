import turtle
import math
def line_without_moving(length):
    turtle.forward(length)
    turtle.backward(length)

for i in range(5):
    turtle.pendown()
    for j in range(4):
        line_without_moving(5)
        turtle.right(90)
    turtle.penup()
    turtle.forward(15)

turtle.exitonclick()