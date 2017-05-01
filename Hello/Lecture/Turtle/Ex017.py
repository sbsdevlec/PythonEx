import turtle
import math
def tilted_square():
  turtle.left(20)     # now we can change the angle only here
  for _ in range(4):
      turtle.forward(50)
      turtle.left(90)

tilted_square()
tilted_square()
tilted_square()

# bonus: you could have a separate function for drawing a square,
# which might be useful later:

def square():
  for _ in range(4):
      turtle.forward(50)
      turtle.left(90)

def tilted_square():
  turtle.left(20)
  square()

turtle.exitonclick()