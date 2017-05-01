# 거북이를 사용하자
import turtle

turtle.register_shape("run.gif")  # 등록가능 gif만 가능
turtle.register_shape("shipping.gif")  # 등록가능 gif만 가능
print(turtle.getshapes())
# turtle.shape('arrow')
#turtle.shape('run.gif') # 사용
turtle.shape('shipping.gif') # 사용
turtle.forward(100)
turtle.right(90) # 회전하지 않는다.
# 일시정지한다.
turtle.done()