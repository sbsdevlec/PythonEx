# 함수의 정의
def viewMessage(message, count=1):
    print("알림 : \"" + str(message) * count + "\"" )

viewMessage("안녕하세요")
viewMessage("에러가 발생했습니다.")
viewMessage("*", 30)
viewMessage(101, 20)
viewMessage(101)

# 변수에 함수 대입
line = viewMessage;
print(type(viewMessage))
print(type(line))

# 변수로 함수 호출
line('-',50)
