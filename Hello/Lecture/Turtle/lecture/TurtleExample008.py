# 거북이를 사용하자
import turtle

turtle.title('거북아놀자')   # 윈도우의 제목을 변경해보자
turtle.shape('turtle')      # 거북이를 나타나게하자

turtle.color('black','red') # 거북이 색상을 변경해보자
turtle.forward(30)
turtle.stamp()                  # 도장을 찍어보자
turtle.color('black','green') # 거북이 색상을 변경해보자
turtle.forward(30)
turtle.stamp()
turtle.color('black','yellow')
turtle.forward(30)
turtle.stamp()
turtle.color('black','blue')
turtle.forward(30)
turtle.stamp()

# 클릭시 종료되게 하자
turtle.exitonclick()
