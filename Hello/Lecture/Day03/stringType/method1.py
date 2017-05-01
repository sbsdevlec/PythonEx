"""
문자열 str 클래스에는 여러 유용한 메서드들이 제공되고 있는데, 이 중 흔히 사용되는 몇가지만 알아보고 넘어가자
"""
str1 = '1,2,3,4,5,6,7,8,9,10'
print(str1, type(str1))
str2 = '1,2,3,4,5,6,7,8,9,10'.split(',') #  특정 separator를 기준으로 문자열을 분리하여 리스트를 리턴한다.
print(str2, type(str2))
print(str2[5],str2[2])

str3 = "-".join(str2) # 여러 개의 문자열을 하나로 결합하는 join() 메서드가 있는데, join() 메서드는 문자열을 결합하는데 사용되는 Separator를 join 메서드 앞에 사용한다.
print(str3, type(str3))
str3 = '/'.join(str2)
print(str3, type(str3))
str3 = '\n'.join(str2)
print(str3, type(str3))

#천단위마다 ,찍기
value = 1234435577
print("{:,}".format(value))

str4 = "-".join('가나다라마바사아')
print(str4)
str4 = "".join('가, 나, 다, 라, 마, 바, 사, 아'.split(', '))
print(str4)
str4 = "".join('가, 나, 다, 라, 마, 바, 사, 아'.split(','))
print(str4)

