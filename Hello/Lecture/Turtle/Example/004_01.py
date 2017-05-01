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
turtle.right(180)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.rt(90)
turtle.fd(100)
turtle.rt(90)
turtle.fd(100)

turtle.fd(100)
turtle.lt(90)
turtle.fd(100)
turtle.lt(90)
turtle.fd(100)
turtle.lt(90)
turtle.fd(100)

turtle.rt(45)

# 일시정지한다.
turtle.done()