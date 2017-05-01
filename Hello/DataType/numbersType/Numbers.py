'''
Numbers
'''
"""
파이썬 3는 정수형(integer)과 실수형(floating point number)을 지원합니다.
파이썬은 변수 선언시 타입을 별도로 선언하지 않기 때문에,
정수형인지 실수형인지를 판단하려면 값에 소숫점이 있는지 없는지를 봐야합니다.
"""
# 타입 검사
print(type(1))
print(type(1.))
print(type(1.0))
print(type(.0))
print("="*50)

# isinstance() 함수를 사용하면,
# 첫번째 파라미터로 넘겨진 값이나 변수가 두번째 파라미터로 넘겨진 타입과 같은지 아닌지를 알 수 있습니다.
print( isinstance(1, int) )
print( isinstance(1, float) )
print( isinstance(1., float) )
print( isinstance(.1, float) )
print("="*50)

# 정수에 정수를 더하면 정수입니다.
# 정수에 실수를 더하면 실수입니다.
# 실수에 실수를 더하면 실수입니다.
# 파이썬에선 정수와 실수를 더하면, 먼저 정수를 실수로 변경한 후 연산을 적용합니다. 따라서 연산결과는 실수입니다.
print(1 + 1, type(1+1))
print(1 + 1.0, type(1+1.0))
print(1.0 + 1, type(1.0+1))
print(1.0 + 1.0, type(1.0+1.0))
print("="*50)

# 정수와 실수간 변환하기
print( float(3))
#print( (float)2 )
print( int(3.0) )
# 실수는 소숫점 아래 15 자리까지만 표현할 수 있습니다.
print(1.12345678901234567890)
print(1.12345678901234512345)
print(1.12345678901234545454)
# 정수는 임의의 큰 수를 표현하는데 사용합니다.
print(1234567890123456789012345678901234567890)
print("="*50)

"""
파이썬 2에서는 int 형과 long 형을 따로 정의해 두었습니다.
int 형의 크기는 sys.maxint 에 정의되어 있고요.
물론 윈도우인지 리눅스인지, 32비트인지 64비트인지 같은 OS 플랫폼에 따라 달라지긴 하지만,
int 형의 크기는 최소한 2의 32-1승 입니다.
파이썬 3에서는 long 형을 따로 두지 않고, 모든 정수는 int 형 하나로 표시합니다.
자세한 내용은 pep 237 를 읽어 보세요.
"""
import sys

t1 = sys.maxsize
t2 = sys.maxsize+1 #이것도 type int

print(t1)
print(t2)
print(type(t1))
print(type(t2))
print(isinstance(t2,int))
#print(isinstance(t2,long))
"""
python 2의 경우
9223372036854775807
9223372036854775808
<type 'int'>
<type 'long'>
"""
print("="*50)

# 정수화
import math
# int : 소수점 버림
print("int***************")
print( int(3.5) )
print( int(-3.5) )
# floor : 인수값을 넘지 않는 최대 정수
print("floor ***************")
print( math.floor(3.5) )
print( math.floor(-3.5) )
# ceil : 인수값을 넘는 최소 정수
print("ceil ***************")
print( math.ceil(3.5) )
print( math.ceil(-3.5) )
print("="*50)
# round : 반올림
print("round ***************")
print( round(3.5) )
print( round(-3.5) )
print( round(3.45678,2) )
print( round(-3.45678,4) )
print( round(56789) )
print( round(56789,-1) )
print("="*50)
for len in range(-1,-5,-1):
    print( round(56789,len) )

# 올림,버림은 어떻게?
print("="*50)

# 간단한 연산
x=10
y=3
print( x + y)
print( x - y)
print( x * y)
print( x / y)
print( x // y)  # 주의  3
print( x % y)   # 주의  1
print( x ** y)
print("="*50)
x=-10
y=3
print( x + y)
print( x - y)
print( x * y)
print( x / y)
print( x // y) # 주의  -4
print( x % y)  # 주의   2
print( x ** y)
print("="*50)
"""
/ 연산자는 실수 나눗셈을 합니다. 분모와 분자 모두 int형이더라도 결과는 항상 float 형이 됩니다.
// 연산자는 조금 독특한 정수 나눗셈을 합니다. 만약 결과가 양수라면 소숫점 이하는 무조건 버립니다.
하지만, 조심할게 있습니다.
만약 // 연산자를 음수에 적용하면, 소숫점 이하는 역시 버리고, 결과를 가장 가까이 있는 자기보다 적은 정수값으로 만듭니다.
결과만 놓고 볼 때는, −5 보다 −6이 더 작으니까, 수학적으로 말하면 반내림과 같습니다.
-5 라고 자신있게 말씀하셨던 분 많죠? 앞에서 조심하라고 말씀드렸었죠?
// 연산자의 결과값이 언제나 정수형인 것은 아닙니다.
분자와 분모 중 하나가 실수형이면, 결과값도 실수입니다. 하지만 실수인 결과값 역시 가장 가까운 작은 정수로 변환됩니다.
"""
print(3//2)
print(-3//2)
print(10//3)
print(-10//3)
print("="*50)
"""
계산 결과 확인 요망
"""
print(3%2)
print(-3%2)
print(10%3)
print(-10/3)
print(-10%3)
print(10%4)
print(-10/4)
print(-10%4)
print(10%6)
print(-10/6)
print(-10%6)
print(10%9)
print(-10/9)
print(-10%9)
print("="*50)
# 분수 다루기
import fractions
x = fractions.Fraction(1, 3)
print(x)
x *= 2
print(x)
print( fractions.Fraction(6, 4))
# print( fractions.Fraction(6, 0)) #ZeroDivisionError: Fraction(6, 0)
print("="*50)

# 진법의 표현
i = 100
print("i = ", i)
i = 0b100
print("i = ", i)
i = 0o100
print("i = ", i)
i = 0x100
print("i = ", i)
print("="*50)
print("i = ", bin(i))
print("i = ", int(i))
print("i = ", oct(i))
print("i = ", hex(i))
print()
i="111"
print("i = ", int(i))
print("i = ", int(i,2))
print("i = ", int(i,8))
print("i = ", int(i,16))
print("i = ", int(i,5))
print("="*50)
