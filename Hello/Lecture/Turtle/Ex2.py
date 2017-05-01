import turtle

scr = turtle.Screen()
square_pants = turtle.Turtle()
square_pants.shape("turtle")
square_pants.pensize(10)
colours = ["red", "green", "blue", "cyan"]

square_pants.penup()

for colour in colours:
    square_pants.color(colour)
    square_pants.forward(100)
    square_pants.left(90)
    square_pants.stamp()

turtle.exitonclick()