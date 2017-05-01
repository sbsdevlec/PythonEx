# 거북이를 사용하자
import turtle

# 커서를 거북이로 만들자
turtle.shape('turtle')

print(turtle.color())
turtle.color('red')
print(turtle.color())
turtle.forward(50)
# 도장을 찍자
turtle.stamp()

turtle.color("red", "green")
print(turtle.color())
turtle.forward(50)
turtle.stamp()

turtle.color("#285078", "#a0c8f0")
print(turtle.color())
turtle.forward(50)
turtle.stamp()

# 일시정지한다.
turtle.done()