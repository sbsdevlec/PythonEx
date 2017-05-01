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
turtle.backward(100)
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
# 원점으로 가라
turtle.home()

# 일시정지한다.
turtle.done()