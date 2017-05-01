# 추가, 수정, 삭제, 읽기
dataMap = {1:('한사람',32),2:('두사람',22)}
print(dataMap)
# 추가
dataMap[3] = ('세사람',21)
dataMap[4] = ('네사람',51)
print(dataMap)
# 수정
dataMap[3] = ('세사람',35)
print(dataMap)
dataMap[3] = ('오사람',34)
print(dataMap)

# 삭제
del dataMap[3]
print(dataMap)

# 읽기
for key in dataMap:
    print(key , ":" , dataMap[key])

# keys메서드
# dict 클래스의 keys()는 Dictonary의 키값들로 된 dict_keys 객체를 리턴
keys = dataMap.keys()
print(type(keys))
print(keys)
for k in keys:
    print(k)

# values메서드
# values()는 Dictonary의 값들로 된 dict_values 객체를 리턴
values = dataMap.values()
print(type(values))
print(values)
for v in values:
    print(v)

# items 메서드
# dict의 items()는 Dictonary의 키-값 쌍 Tuple 들로 구성된 dict_items 객체를 리턴
items = dataMap.items()
print(type(items))
print(items)
for v in items:
    print(v)

# dict_items를 리스트로 변환할 때
itemsList = list(items)
print(itemsList)