def myFunction1():
    print("myFunction1 에서 전역변수 출력", x)

def myFunction2():
    print("myFunction2 에서 전역변수 출력", x)
    y = x * 2 # 전역변수를 사용하여 연산 수행
    print("myFunction2 에서 지역변수 출력", y)

def myFunction3():
    # 대입연산자를 사용하면 무조건 지역변수로 인식한다.
    # print("myFunction2 에서 전역변수 출력", x) # 초기화 되지 않은 지역변수 사용 에러
    x =  10 # 여기서 전역변수와 같은 이름의 변수를 사용하면 지역변수로 인식
    print("myFunction3 에서 지역변수 출력", x)

def myFunction4():
    global x;
    x =  10 # 여기서 전역변수와 같은 이름의 변수를 사용하면 지역변수로 인식
    print("myFunction4 에서 전역변수 출력", x)

def myFunction5(x): # 인수로 받은 변수도 지역변수
    print("myFunction5 시작", x)
    x += 20;
    print("myFunction5 종료", x)

x = 2 # 전역변수
print("myFunction1 함수 호출 전", x)
myFunction1()
print("myFunction1 함수 호출 후", x)
print()
myFunction2()
print()
myFunction3()
print()
print("myFunction4 함수 호출 전", x)
myFunction4()
print("myFunction4 함수 호출 후", x)
print()

print("myFunction5 함수 호출 전", x)
myFunction5(x)
print("myFunction4 함수 호출 후", x)
