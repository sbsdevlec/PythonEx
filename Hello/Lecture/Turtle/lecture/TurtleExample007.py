# 거북이를 사용하자
import turtle

turtle.title('거북아놀자')   # 윈도우의 제목을 변경해보자
turtle.color('black','red') # 거북이 색상을 변경해보자
turtle.shape('turtle')      # 거북이를 나타나게하자

turtle.forward(100)     # 앞으로 100 이동
turtle.left(90) # 왼쪽(시계방향)으로 방향전환
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

# 클릭시 종료되게 하자
turtle.exitonclick()
