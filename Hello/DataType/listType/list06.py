import random
list=[]
for i in range(1,30):
    list.append(random.randrange(1,11))
print(list)

# 리스트에 포함된 요소 x의 개수 세기(count)
print(list.count(5))

list1 = [1,2,3]
list2 = [4,5,6]
print(list1)
print(list2)
list1.extend(list2)
print(list1)
print(list2)

# 리스트 연산
list3 = [1,2,3]
list4 = [4,5,6]
print(list3)
print(list4)
list5 = list3 + list4
print(list5)
list6 = list3 * 3
print(list6)
print("*" * 30)

# list1.extend(list2) 는 list1 += list2와 같다
# list1 = list1 + list2과 같다
