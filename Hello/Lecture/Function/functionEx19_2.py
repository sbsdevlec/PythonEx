def myFunction2():
    print("myFunction2 에서 전역변수 출력", x)
    y = x * 2 # 전역변수를 사용하여 연산 수행하고 지역변수 y에 대입
    print("myFunction2 에서 지역변수 출력", y)

x = 2 # 전역변수
print('전역변수 x의 값 : {}'.format(x))
myFunction2()
print('전역변수 x의 값 : {}'.format(x))
# print('지역변수 y의 값 : {}'.format(y)) # NameError: name 'y' is not defined
print()
