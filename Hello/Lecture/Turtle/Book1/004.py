import turtle
def init(width,height):
    screen = turtle.Screen()
    screen.title('거북이 프로그램')
    screen.setup(width+50, height+50)
    screen.screensize(width,height)
    turtle.penup()
    turtle.goto(-width/2, height/2)
    turtle.pendown()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.penup()
    turtle.home()
    turtle.pendown()
# -----------------------------------------------
init(800, 600)
# -----------------------------------------------
# 여기에서 작업을 하자~~~~~


# -----------------------------------------------
turtle.exitonclick()
# -----------------------------------------------
