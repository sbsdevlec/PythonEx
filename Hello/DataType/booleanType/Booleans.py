'''
Booleans
'''
"""
Boolean은 참 이나 거짓 가운데 하나를 의미하는 데이터 타입입니다.
파이썬은 이를 위해 True 와 False 라는 상수를 정의해서 사용하고,
이 상수를 변수에 직접 할당하여 Boolean 타입으로 만들 수 있습니다.
어떤 상황에서는, 주어진 표현식이 반드시 True 이거나 False 여야 합니다.
"""

print(True)
print(False)
#print(true)
#print(false)
#print(TRUE)
#print(FALSE)
print("="*50)

print(1==1)
print(1==2)
print("="*50)

print(type(True))
print(type(False))
print(type(1==1))
print(type(1==2))
print("="*50)

print(not False)
print(not True)
print(not not True)
print("="*50)

size=1
print(size<0)
print(size>0)
print(size==1)
print("="*50)

# python의 3항 연산자 사용
print("참" if "" else "거짓")
print("참" if "0" else "거짓")
print("참" if 0 else "거짓")
print("참" if 1 else "거짓")
print("참" if -1 else "거짓")
print("참" if None else "거짓") # null의 표현
print("="*50)

# null의 판단
a=0
print(None)
print(type(None)) # <class 'NoneType'>
print(not None)
print(a is None)
print(a is not None)
print("="*50)

# True/False 연산
# True는 1, False는 0을 의미합니다.
print(True + True)
print(True + False)
print(False + False)
print(True + 0)
print(False + 0)
print(True - True)
print(True * False)
print(True / True)
# print(True / False) # ZeroDivisionError: division by zero
print("="*50)

