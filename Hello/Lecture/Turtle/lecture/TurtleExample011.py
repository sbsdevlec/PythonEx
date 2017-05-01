# 거북이를 사용하자
import turtle
turtle.title('거북아놀자')   # 윈도우의 제목을 변경해보자
turtle.color('black','red') # 거북이 색상을 변경해보자
# turtle.shape('turtle')      # 거북이를 나타나게하자

# 함수 정의
def move(length):
    turtle.penup()
    turtle.forward(length)
    turtle.pendown()

move(-350)
for i in range(3,15):
    turtle.begin_fill()
    turtle.circle(28,steps=i)
    move(60)
    turtle.end_fill()

# 클릭시 종료되게 하자
turtle.exitonclick()
