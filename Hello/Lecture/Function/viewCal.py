w = ("일", "월", "화", "수", "목", "금", "토")
# 윤년/평년을 판단하는 함수
def isLeapYear(year):
    return year%400==0 or year%4==0 and year%100!=0

# 월의 마지막 날짜를 구해주는 함수
def lastday(year, month):
    m = [31,28,31,30,31,30,31,31,30,31,30,31]
    m[1] = 29 if isLeapYear(year) else 28
    return m[month-1]

# 총일수를 구해주는 함수
def sumday(year,month,date):
    s = (year-1)*365 + (year-1)//4 - (year-1)//100 + (year-1)//400
    for m in range(1,month):
        s+= lastday(year,m)
    s += date
    return s

# 요일을 숫자로 알려주는 함수
def weekday(year,month,day):
    return sumday(year,month,day)%7

# 요일을 문자열로 알려주는 함수
def strweekday(year,month,day):
    return w[sumday(year,month,day)%7]

# 달력을 출력해주는 함수
def viewCalendar(year,month):
    print("\n{0:18d}년 {1:02d}일\n".format(year,month))
    for i in w: print("{:>4}".format(i),end='')
    print()
    for i in range(weekday(year,month,1)) : print("{:>5}".format(''),end='')
    for i in range(1,lastday(year,month)+1):
        print("{:>5}".format(i), end='')
        if weekday(year,month,i)==6: print()
    print("\n")

# 현재 날짜 구하기
import datetime
now = datetime.datetime.now()
print(now)
yy  = now.year
mm = now.month
dd = now.day
print("오늘 : {}년 {}월 {}일".format(yy,mm,dd))

print("총일수 ", sumday(yy,mm,dd))
print("요일", weekday(yy,mm,dd))
print("요일", strweekday(yy,mm,dd))

print("1년 1월 1일 태어난 당신이 살아온 일수는 총", sumday(yy,mm,dd) - sumday(1,1,1) + 1,"일 입니다.")
print("1992년 8월 22일 태어난 당신이 살아온 일수는 총", sumday(yy,mm,dd) - sumday(1992,8,22) + 1,"일 입니다.")
print("올해는 총", sumday(yy,mm,dd) - sumday(yy,12,31) ,"일 남았습니다.")

viewCalendar(yy,mm)
