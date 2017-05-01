import turtle
import math
def line_without_moving(length):
    turtle.forward(length)
    turtle.backward(length)

def star_arm(length):
    line_without_moving(length)
    turtle.right(360/5)
    #turtle.right(360/4)

for _ in range(5):
    star_arm(10)

turtle.exitonclick()