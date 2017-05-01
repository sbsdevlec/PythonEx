"""
튜플(tuple)은 몇 가지 점을 제외하곤 리스트와 거의 비슷하며 리스트와 다른 점은 다음과 같다.
리스트는 [과 ]으로 둘러싸지만 튜플은 (과 )으로 둘러싼다.
리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.
"""

#  swap
a=1
b=2
print(a,b)
t = a
a = b
b = t
print(a,b)

# swap
a = a ^ b
b = a ^ b
a = a ^ b
print(a,b)

# swap
a,b = b,a # 튜플대입을 처리
print(a,b)

'''
a,b = b,a 에서  등호 왼쪽도 오른쪽도 튜플
'''
t1 = 1,2,3
t2 = t1 # 튜플대입
print(t1)
print(t2)
t2 = 3,1,2,1,2,3
print(t2)
t1 = t2
print(t1)
print(t2)

t3 = 11,22,33
t4 = 44,55,66
print(t3)
print(t4)
t3,t4 = t4,t3
print(t3)
print(t4)

import random
a = random.sample(range(1,101),10)
print(a, type(a))

b = tuple(a)
print(b, type(b))


