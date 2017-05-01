# 리스트에 추가하기
list = []
print(list)
list.append(9)
list.append(8)
list.append(7)
print(list)
list.append([6,5,4]);
print(list)
print("*"*30)

# 리스트 수정하기
list[0] = 88
print(list)
list[1:2] = [77,66,55,44]
print(list)
#list[1:5] = 33 # TypeError: can only assign an iterable
list[1:5] = [33]
print(list)
print("*"*30)

# 리스트 삭제하기
del list[0]
print(list)
del list[0:1]
print(list)
list[1][:2]=[]
print(list)
list[1]=[]
print(list)
list[1]=[1,2,3]
print(list)
del list[1]
print(list)
print("*"*30)

# 리스트에 삽입하기
list.insert(0,6)
list.insert(0,7)
print(list)
list.insert(1,[2,2,2])
print(list)
print("*"*30)

# 리스트 확장
list[0:]=[1,2,3,4,5]
print(list)
list.append(11)
list.append(12)
list.append(13)
print(list)
list.extend([21,22,23])
print(list)
append = [33,44,55,66,77]
list.extend(append)
print(list)
