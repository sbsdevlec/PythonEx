import turtle
import math

def make_window(colr, ttle):
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w

def make_turtle(colr, sz):
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t

def draw_rectangle(t, w, h):
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

def draw_square(tx, sz):
    draw_rectangle(tx, sz, sz)

wn = make_window("lightgreen", "Tess and Alex dancing")
tess = make_turtle("hotpink", 5)
alex = make_turtle("black", 1)
dave = make_turtle("yellow", 2)

draw_rectangle(tess,100,150)
draw_square(alex,200)
draw_square(dave,300)

turtle.exitonclick()