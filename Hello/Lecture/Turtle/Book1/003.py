import turtle

def init():
    screen = turtle.Screen()
    screen.title('거북이 프로그램')
    screen.setup(650, 650)
    screen.screensize(600, 600)
    width, height = screen.screensize()
    turtle.penup()
    turtle.goto(-width/2, height/2)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(width)
        turtle.right(90)
    turtle.penup()
    turtle.home()
    turtle.pendown()
# -----------------------------------------------
init()

turtle.exitonclick()
