# x = 2 # 함수의 정의 위에 있든 아래에 있든 함수 밖에서 선언하면 전역변수이다.

def myFunction1():
    print("myFunction1 에서 전역변수 출력", x)

x = 2 # 전역변수. 함수에서 사용하려면 호출 전에 선언이 되어있어야 함
print("myFunction1 함수 호출 전", x)
myFunction1()
# x = 2 # 변수를 선언 전에 사용하면  Error : NameError: name 'x' is not defined
print("myFunction1 함수 호출 후", x)
print()