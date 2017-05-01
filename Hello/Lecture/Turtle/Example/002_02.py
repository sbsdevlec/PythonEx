# 거북이를 사용하자
import turtle

shapes = turtle.getshapes()
# 커서를 거북이로 만들자
for shape in shapes:
    print(shape)
    turtle.shape(shape)
    # 앞으로 0만큼이동
    turtle.forward(0)
    turtle.delay(500)
    turtle.clear()
# 일시정지한다.
turtle.done()