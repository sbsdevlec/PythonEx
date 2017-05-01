name="한사람"
age=34
gender=True
height = 178.7

str  = "{}님의 나이는 {}세입니다.".format(name,age)
print(str)
str  = "{0}님의 나이는 {1}세입니다.".format(name,age)
print(str)
str  = "{0}님 {0}님은 정말 천재입니다.\n{0}님 만나서 반가워요!!".format(name)
print(str)
str  = "{name}님의 나이는 {age}세입니다.".format(name=name,age=age)
print(str)
str  = "{0}님의 나이는 {1}세(성별 : {gender})입니다.".format(name,age, gender=gender)
print(str)
str  = "{0}님의 나이는 {1}세(성별 : {gender})입니다.".format(name,age, gender="남" if gender else "여")
print(str)
str  = "{!r}님의 나이는 {}세입니다.".format(name,age)    # repr()
print(str)
str  = "{!a}님의 나이는 {}세입니다.".format(name,age)    # ascii()
print(str)
str  = "{!s}님의 나이는 {}세입니다.".format(name,age)    # str()
print(str)

# {}를 표시하려면 {{ , }}로 입력
a = 5
b = 9
setStr = '{{{}, {}}}'.format(a, b)
print(setStr)

