import turtle
t = turtle.Turtle()        # 거북이 객체 생성

t.pensize(3)               # 펜 크기를 3으로 
t.pendown()              # 펜을 내린다 (그릴 준비)
t.circle(40, steps=3)    # 반지름 40인 원을 3번의 직선으로 그린다. = 삼각형

t.penup()                  # 펜을 올린다. (그리지 않음)
t.goto(-100, -50)
t.pendown()
t.circle(40, steps=4)    # 4각형

t.penup()
t.goto(0, -50)
t.pendown()
t.circle(40, steps=5)    # 5각형

t.penup()
t.goto(100, -50)
t.pendown()
t.circle(40, steps=6)

t.penup()
t.goto(200, -50)
t.pendown()
t.circle(40, steps=40)    # 원

turtle.done()