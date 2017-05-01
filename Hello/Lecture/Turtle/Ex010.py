import turtle
turtle.colormode(255)
turtle.color(215, 100, 170)
turtle.shape("turtle")

for i in range(4):
    turtle.left(90)
    turtle.forward(100)
for i in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.exitonclick()
