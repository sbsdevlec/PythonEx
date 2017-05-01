import datetime
# 멤버가 __로 시작하면 private이고 기본적으로 public이다.
class MyDate:
    def __init__(self):
        now = datetime.datetime.now()
        self.__yy = now.year
        self.__mm = now.month
        self.__dd = now.day
    def __makeStr(self):
        return "{}년 {}월 {}일".format(self.__yy, self.__mm, self.__dd)
    def __str__(self):
        return self.__makeStr()

today = MyDate()
print(today)
# print(today.__makeStr()) # 에러 : AttributeError: 'MyDate' object has no attribute '__makeStr'
# print(today.__yy) # 에러 : AttributeError: 'MyDate' object has no attribute '__yy'
