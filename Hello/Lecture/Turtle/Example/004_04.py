# 거북이를 사용하자
import turtle

# 커서를 거북이로 만들자
turtle.shape('turtle')
'''
이동하는 메서드를 배우자
turtle.forward(distance)
turtle.fd(distance)

turtle.back(distance)
turtle.bk(distance)
turtle.backward(distance)

turtle.right(angle)
turtle.rt(angle)

turtle.left(angle)
turtle.lt(angle)

'''
angle = 180 - 720/6
print(angle)
turtle.forward(100)
turtle.left(angle)
turtle.forward(100)
turtle.left(angle)
turtle.forward(100)
turtle.left(angle)
turtle.forward(100)
turtle.left(angle)
turtle.forward(100)
turtle.left(angle)
turtle.home() # 원점으로 가라

turtle.forward(100)
turtle.right(angle)
turtle.forward(100)
turtle.right(angle)
turtle.forward(100)
turtle.right(angle)
turtle.forward(100)
turtle.right(angle)
turtle.forward(100)
turtle.right(angle)
turtle.home() # 원점으로 가라

# 일시정지한다.
turtle.done()