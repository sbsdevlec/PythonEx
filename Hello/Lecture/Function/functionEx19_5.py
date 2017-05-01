def myFunction5(x): # 인수로 받은 변수도 지역변수
    print("myFunction5 시작", x)
    x += 20;
    print("myFunction5 종료", x)

x = 2 # 전역변수
print("myFunction5 함수 호출 전", x)
myFunction5(x)
print("myFunction4 함수 호출 후", x)
