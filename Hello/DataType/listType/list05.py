import random
list=[]
for i in range(1,30):
    list.append(random.randrange(1,11))
print(list)

# 개수세기
for i in range(1,11):
    print( i , "의 개수", list.count(i))

# 정렬
list.sort()
print(list)
list.sort(reverse=True)
print(list)
t = sorted(list)
print(t)
print(list)
print("*" * 30)

# 뒤집기
list.reverse()
print(list)
list.reverse()
print(list)
print("*" * 30)

# 첫번째 요소 제거하기
list.remove(9)
print(list)

# 첫번째 요소 위치구하기
print(list.index(6))
print(list.index(10))
# print(list.index(11)) # ValueError: 11 is not in list

print(list.pop())
print(list.pop())

while len(list):
    print(list.pop())


