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
    turtle.hideturtle()
    turtle.home()
# -----------------------------------------------
init(800, 600)
# -----------------------------------------------
# 여기에서 작업을 하자~~~~~
redTurtle = turtle.Turtle()
redTurtle.shape('turtle')
redTurtle.color('black','red')
redTurtle.forward(50)

greenTurtle = turtle.Turtle()
greenTurtle.shape('turtle')
greenTurtle.color('black','green')
greenTurtle.left(90)
greenTurtle.forward(50)

yellowTurtle = turtle.Turtle()
yellowTurtle.shape('turtle')
yellowTurtle.color('black','yellow')
yellowTurtle.right(180)
yellowTurtle.forward(50)

blueTurtle = turtle.Turtle()
blueTurtle.shape('turtle')
blueTurtle.color('black','blue')
blueTurtle.right(90)
blueTurtle.forward(50)

# -----------------------------------------------
turtle.exitonclick()
# -----------------------------------------------
