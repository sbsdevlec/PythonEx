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

move(-300,300)
for _ in range(10):
    myTurtle.dot()
    myTurtle.forward(50)

move(-300,250)
for i in range(10):
    myTurtle.dot(i*5)
    myTurtle.forward(50)

move(-300,200)
colors = ['red','blue','green','silver','navy','yellow']
for i in range(10):
    myTurtle.dot(i*5, colors[i%6])
    myTurtle.forward(50)

screen.mainloop()