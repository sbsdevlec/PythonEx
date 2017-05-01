import turtle
def init(width,height):
    screen.setup(width + 50, height + 50)
    screen.screensize(width, height)
    turtle.penup()
    turtle.goto(-width/2, height/2)
    turtle.pendown()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.penup()
    turtle.ht()
    turtle.home()
# -----------------------------------------------
screen = turtle.Screen()
screen.title('거북이 프로그램')
init(600, 600)
moveTurtle = turtle.Turtle()
# -----------------------------------------------
def move():
    moveTurtle.forward(10)

def rotate():
    moveTurtle.left(45)

def quit():
    screen.bye()

screen.onkey(move, "Right")
screen.onkey(rotate, "space")

# 종료지정
screen.onkey(quit, "q")
screen.onkey(quit, "Q")
# -----------------------------------------------
screen.listen()
screen.mainloop()
# -----------------------------------------------