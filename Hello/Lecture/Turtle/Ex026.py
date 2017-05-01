import turtle
import math

def draw_rectangle(t, w, h):
    """Get turtle t to draw a rectangle of width w and height h."""
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

def draw_square(tx, sz):        # A new version of draw_square
    draw_rectangle(tx, sz, sz)

def draw_multicolor_square(tx, sz):        # A new version of draw_square
    for color in ['red','purple','hotpink','blue']:
        tx.color(color)
        tx.forward(sz)
        tx.left(90)

wn = turtle.Screen()        # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()      # Create tess and set some attributes
tess.pensize(3)

draw_rectangle(tess,200,160)
draw_square(tess,100)
draw_multicolor_square(tess, 150)

turtle.exitonclick()