"""
003 포맷 연산자
print 함수를 사용하여 3.141592의 값을 출력하라. 단, 출력된 값이 소수점 아래로 두 자리 숫자까지만 표시되도록 하라.
"""
d = 3.141592
print(d)
print(int(d*100)/100)
print("{0}".format(d))
print("{0:.2f}".format(d))
print("%.2f"%(d))
print(d)
print("*"*50)

d =3.45678
print(d)
print(int(d*100)/100)
print("{0}".format(d))
print("{0:.2f}".format(d))
print("%.2f"%(d))
print(d)
print("*"*50)
