# 거북이를 사용하자
import turtle
turtle.title('거북아놀자')   # 윈도우의 제목을 변경해보자
turtle.color('black','red') # 거북이 색상을 변경해보자
turtle.shape('turtle')      # 거북이를 나타나게하자

# 함수 정의
def move(length):
    turtle.penup()
    turtle.forward(length)
    turtle.pendown()

move(-200) # 함수호출
for _ in range(4): # 반복문
    turtle.forward(50)     # 앞으로 100 이동
    turtle.left(90) # 왼쪽(시계방향)으로 방향전환

move(100)
colors = ['red','green','yellow', 'blue'] # 리스트
for color in colors:
    turtle.color('black',color) # 거북이 색상을 변경해보자
    turtle.forward(50)
    turtle.stamp()

move(150)
for i in range(3):
    turtle.left(120)
    turtle.color('black', colors[i])  # 거북이 색상을 변경해보자
    turtle.forward(100)
    turtle.stamp()  # 도장을 찍어보자

# 클릭시 종료되게 하자
turtle.exitonclick()
