import turtle
screen = turtle.Screen()
myTurtle = turtle.Turtle()

def init(width, height):
    screen.title('거북이 프로그램')
    screen.setup(width + 50, height + 50)
    screen.screensize(width, height)

def move(x,y):
    myTurtle.pu()
    myTurtle.goto(x, y)
    myTurtle.pd()

init(600, 600)

myTurtle.circle(50)

myTurtle.penup()
myTurtle.setposition(-120, 0)
myTurtle.pendown()
myTurtle.circle(50)

myTurtle.penup()
myTurtle.setposition(60, 60)
myTurtle.pendown()
myTurtle.circle(50)

myTurtle.penup()
myTurtle.setposition(-60, 60)
myTurtle.pendown()
myTurtle.circle(50)

myTurtle.penup()
myTurtle.setposition(-180, 60)
myTurtle.pendown()
myTurtle.circle(50)

screen.mainloop()