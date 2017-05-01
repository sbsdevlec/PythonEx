def myFunction4():
    global x; # 전역변수 x를 사용하겠다.
    x +=  10  # 전역변수로 인식
    print("myFunction4 에서 전역변수 출력", x)

x = 2 # 전역변수
print("myFunction4 함수 호출 전", x)
myFunction4()
print("myFunction4 함수 호출 후", x)
print()
