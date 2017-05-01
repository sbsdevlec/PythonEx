class Person:
    pass

s = Person()
print(vars(s))
s.name = "한사람"
print(vars(s))
s.age=33
print(vars(s))

print(type(s))
# import가 아니고 파이썬 인터프리터가 최초로 파일을 읽어서 실행하는 경우를 살펴보자.
# 파이썬 인터프리터는 소스파일을 읽고, 그 안의 모든 코드를 실행하게 되는데, 코드를 실행하기 전에 특정한 변수값을 정의한다.
# 그중 하나가 __name__ 이라는 변수를 __main__ 으로 세팅을 한다.
# print(__name__=='__main__')


