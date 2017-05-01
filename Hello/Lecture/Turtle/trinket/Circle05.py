import turtle
screen = turtle.Screen()
def init(width, height):
    screen.title('거북이 프로그램')
    screen.setup(width + 50, height + 50)
    screen.screensize(width, height)

init(800, 600)

turtle.back(300)
turtle.circle(30)
for i in range(4):
    turtle.forward(30)
    turtle.circle(30, 90)

turtle.forward(100)
turtle.circle(30, 90)
turtle.right(90)
turtle.circle(30, 180)
turtle.right(180)
turtle.circle(30, 270)
turtle.penup()
turtle.home()
turtle.pendown()
for i in range(3, 10):
    turtle.circle(20,360,i)
    turtle.penup()
    turtle.forward(60)
    turtle.pendown()

turtle.exitonclick()
