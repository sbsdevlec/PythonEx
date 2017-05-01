def function():
    function.__gender = '남자'

# 타입을 알려준다.
print(type(function))
# 함수도 객체이다.
print(function.__class__.__bases__)
# 모듈이나 클래스 처럼__dict__ 속성을 갖고 있는 객체의 __dict__ 속성들을 리턴해 준다.
print(vars(function))
# dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여줍니다.
# print(dir(function))


function.name='한사람'
function.age=33
print(function.__dict__)
print(vars(function))
print(function.name)
print(function.age)
print(dir(function))


