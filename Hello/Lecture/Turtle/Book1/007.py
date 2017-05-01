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
init(600, 600)
# -----------------------------------------------
# 여기에서 작업을 하자~~~~~
redTurtle = turtle.Turtle()
redTurtle.shape('turtle')
redTurtle.color('black','red')

greenTurtle = turtle.Turtle()
greenTurtle.shape('turtle')
greenTurtle.color('black','green')

yellowTurtle = turtle.Turtle()
yellowTurtle.shape('turtle')
yellowTurtle.color('black','yellow')

blueTurtle = turtle.Turtle()
blueTurtle.shape('turtle')
blueTurtle.color('black','blue')


redTurtle.pu()
redTurtle.goto(-280,280)
redTurtle.right(45)
redTurtle.stamp()

greenTurtle.pu()
greenTurtle.goto(280,280)
greenTurtle.right(135)
greenTurtle.stamp()

yellowTurtle.pu()
yellowTurtle.goto(-280,-280)
yellowTurtle.left(45)
yellowTurtle.stamp()

blueTurtle.pu()
blueTurtle.goto(280,-280)
blueTurtle.left(135)
blueTurtle.stamp()

redTurtle.pd()
redTurtle.goto(-15,15)
# redTurtle.home()
greenTurtle.pd()
greenTurtle.goto(15,15)
# greenTurtle.home()
yellowTurtle.pd()
yellowTurtle.goto(-15,-15)
# yellowTurtle.home()
blueTurtle.pd()
blueTurtle.goto(15,-15)
# blueTurtle.home()


# -----------------------------------------------
turtle.exitonclick()
# -----------------------------------------------
