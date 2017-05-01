def myFunction3():
    # 대입연산자를 사용하면 무조건 지역변수로 인식한다.
    # print("myFunction2 에서 전역변수 출력", x) # 초기화 되지 않은 지역변수 사용 에러
    # x += 10 # 에러 : UnboundLocalError: local variable 'x' referenced before assignment
    x =  10   # 여기서 전역변수와 같은 이름의 변수를 사용하면 지역변수로 인식
    print("myFunction3 에서 지역변수 출력", x)

x = 2 # 전역변수
print("myFunction3 함수 호출 전", x)
myFunction3()
print("myFunction3 함수 호출 후", x)
print()
