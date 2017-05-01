# 거북이를 사용하자
import turtle

# 커서를 거북이로 만들자
turtle.shape('turtle')
turtle.goto(-380, 0)

for red in range(3):
    for green in range(3):
        for blue in range(3):
            turtle.color(red / 4.0, green / 4.0, blue / 4.0)
            turtle.forward(25)
            turtle.stamp()

# 일시정지한다.
turtle.done()