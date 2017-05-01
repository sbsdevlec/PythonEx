# Built-in Functions with Tuple
import random

my_tuple = tuple(random.sample(range(1,100),10))
print(my_tuple)
print(type(my_tuple))

print(all(my_tuple))
print(all(()))
print()

print(any(my_tuple))
print(any(()))
print()

print(enumerate(my_tuple))
for em in enumerate(my_tuple): print(em)

print("길이(len)",len(my_tuple))
print()
print("최대(max)",max(my_tuple))
print()
print("최소(min)", min(my_tuple))
print()

print("최소(min)", min(my_tuple))
print()

print("정렬(sorted)", sorted(my_tuple))
print("정렬(sorted)", sorted(my_tuple, reverse=True))
# 튜플의 요소를 가져 와서 새 정렬 된 목록을 반환합니다 (튜플 자체를 정렬하지 않음).
print(my_tuple)
print()

print("합계(sum)", sum(my_tuple))

"""
temp = tuple("갑을병정무기경신임계")
for em in enumerate(temp):
     print(em[0], " : ", em[1], " : ", type(em))

t1 = tuple("갑을병정무기경신임계")
t2 = tuple("자축인묘진사오미신유술해")
for i in range(0,60):
     print(i+1,t1[i%len(t1)]+t2[i%len(t2)])
"""