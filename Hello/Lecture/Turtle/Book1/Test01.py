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

def makeTurtle(shape, color1, color2):
    tempTurtle = turtle.Turtle()
    tempTurtle.shape(shape)
    tempTurtle.color(color1, color2)
    return tempTurtle

def moveInitTurtle(shape, x,y,angle):
    shape.pu()
    shape.goto(x,y)
    shape.right(angle)
    shape.stamp()

# -----------------------------------------------
turtle.delay(0)
init(600, 600)
# 거북이 만들기
redTurtle = makeTurtle('turtle','black','red')
greenTurtle = makeTurtle('turtle','black','green')
yellowTurtle = makeTurtle('turtle','black','yellow')
blueTurtle = makeTurtle('turtle','black','blue')
# 거북이 이동
moveInitTurtle(redTurtle, -280,280,45)
moveInitTurtle(greenTurtle, 280,280,135)
moveInitTurtle(yellowTurtle, -280,-280,315)
moveInitTurtle(blueTurtle, 280,-280,225)
turtle.delay(10)
# -----------------------------------------------
# 여기에서 작업을 하자~~~~~

redTurtle.pd()
redTurtle.goto(-15,15)
greenTurtle.pd()
greenTurtle.goto(15,15)
yellowTurtle.pd()
yellowTurtle.goto(-15,-15)
blueTurtle.pd()
blueTurtle.goto(15,-15)


# -----------------------------------------------
turtle.exitonclick()
# -----------------------------------------------
