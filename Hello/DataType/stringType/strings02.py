# 문자열 더하기
name = "한사람"
print(name + "씨 방가방가!!!")
age =33;
#print(name + "씨 " + age + "살이네 행님이라 불러~~~")
print(name + "씨 " + str(age) + "살이네 행님이라 불러~~~")

# 문자열 곱하기
print(name*5)
print("_"*30)

# 문자열 다루기
str = "Python Programer"
print("0         1")
print("01234567890123456789")
print(str)
print()

for c in str:
    print(c)
print()

for c in range(0,len(str)):
    print(c , str[c])
print()

# 음수면 뒤에서부터
print(str[0],str[1],str[2])
print(str[-1],str[-2],str[-3])

#문자열 자르기
print(str[0:])      #[n:] : n번쨰 부터 끝까지
print(str[0:1])     #[n:m] : n번째 부터 m전까지
print(str[0:2])
print(str[0:3])
print(str[7:10])
print(str[:6])      #[:n] : 0부터 n전까지
print(str[:])       #[:] : 모두
print(str[3:-8])    # 음수면 뒤에서부터의 위치
print(str[-9:-6])

birth = "920822"
yy = birth[0:2] + "년"
mm = birth[2:4] + "월"
dd = birth[-2:] + "일"
print(yy, mm, dd)

birthday = "{0}년 {1}월 {2}일".format(92,8,22)
print(birthday)
birthday = "{year}년 {month}월 {date}일".format(year=92,month=8,date=22)
print(birthday)


