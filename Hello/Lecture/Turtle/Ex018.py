import turtle
import math
def hexagon():
  for _ in range(6):
      turtle.forward(50)
      turtle.left(60)

for _ in range (6):
    hexagon()
    turtle.forward(50)
    turtle.right(60)

turtle.exitonclick()