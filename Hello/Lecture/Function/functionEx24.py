# 람다함수 : 이름이 없는 함수. 1회성 함수를 바로 만들어서 사용한다.
#            return 구문을 사용할 수 없다. 1줄 실행결과를 바로 리턴함
# lambda 인수들 : 명령문

add = lambda x,y : x+y
print(add(3,5))

isEven = lambda x : x%2==0
print( "짝수" if isEven(5) else "홀수")
print( "짝수" if isEven(6) else "홀수")

isLeapYear = lambda  year : year%400==0 or year%4==0 and year%100!=0

for year in range(2000,2017):
    print(year,"년은 ", "윤년" if isLeapYear(year) else "평년")

