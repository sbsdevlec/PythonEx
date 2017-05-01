a=10
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
print()

print(a==b)
print(a!=b)
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)
print()

print(a|b)
print(a&b)
print(a^b)
print(~b)
print()

print(b<<1)
print(b<<2)
print(b<<3)
print(b>>1)
print(b>>2)
print()

a=True
b=False
print(a and b)
print(a or b)
print(not b)
print()

#맴버 연산자 (Membership Operators)
datas = range(10);
print(type(datas))
print("[", end=" ")
for a in datas:
    print(a, end=" ")
print("]")

a = 5
print( a in datas)
a=15
print( a not in datas)
print()

# 식별 연산자 (Identity Operators): 두 개체의 메모리 위치를 비교한다.
#                                   a = 20, b = 20 이라 가정한다.
import datetime
a = datetime.date
b = a;
print(a)
print(b)
print( a is b)
print( a is not b)
print()
print(type(()))
print(() is ())
print()
print((1,) == (1,))
print((1,) is (1,))
a=(1,)
b=a
print( a is b)
print( a is not b)
print()

a,b=10,20
print(a)
print(b)
a,b=b,a
print(a)
print(b)
