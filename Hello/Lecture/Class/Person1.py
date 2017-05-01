class Person:
    pass

# 동적으로 속성을 추가할 수 있다.
person = Person()
print(vars(person))
person.name = "한사람"
print(vars(person))
person.age=33
print(vars(person))
print(vars(person).keys())
print(person.__dict__)
print(person.__dict__.keys())

print(type(person))
# import가 아니고 파이썬 인터프리터가 최초로 파일을 읽어서 실행하는 경우를 살펴보자.
# 파이썬 인터프리터는 소스파일을 읽고, 그 안의 모든 코드를 실행하게 되는데, 코드를 실행하기 전에 특정한 변수값을 정의한다.
# 그중 하나가 __name__ 이라는 변수를 __main__ 으로 세팅을 한다.
# print(__name__=='__main__')


# var() : 모듈이나 클래스 처럼__dict__ 속성을 갖고 있는 객체의 __dict__ 속성들을 리턴해 준다.
# print(vars(person))
# print(vars(person).keys())
# print(person.__dict__.keys())