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
move(-300,100)
for i in range(6):
    myTurtle.circle((i+1)*10)
    myTurtle.forward((i+1)*10*2+10)
screen.mainloop()