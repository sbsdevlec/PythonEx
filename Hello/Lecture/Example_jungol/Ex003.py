"""
아래와 같이 출력되는 프로그램을 작성하라.
저장예
name="홍길동"
age=13
gender=True

출력예
나의 이름은 "홍길동"입니다.
나의 나이는 '13살'입니다.
나의 성별은 {남자}입니다.
"""
name="홍길동"
age=13
gender=True

print('나의 이름은 "{}"입니다.'.format(name))
print('나의 이름은 "{0}"입니다.'.format(name))
print("나의 이름은 \"{}\"입니다.".format(name))
print("나의 이름은 \"" + name + "\"입니다.")
print("나의 나이는 '{}살'입니다.".format(age))
print("나의 성별은 {{{0}}}입니다.".format("남자" if gender else "여자"))