# 리스트 인덱싱
list1 = [11,22,33,44,55,66,77,88,99,00]
print(list1)        # [11, 22, 33, 44, 55, 66, 77, 88, 99, 0]
print(list1[0])     # 11
print(list1[3])     # 44
print(list1[-1])    #  0
print(list1[-3])    # 88

# 리스트 슬라이싱
print(list1[0:1])   # [11]
print(list1[0:2])   # [11, 22]
print(list1[0:3])   # [11, 22, 33]
print(list1[1:3])   # [22, 33]
print(list1[:3])    # [11, 22, 33]
print(list1[3:])    # [44, 55, 66, 77, 88, 99, 0]
print(list1[-5:])   # [66, 77, 88, 99, 0]
print(list1[:-3])   # [11, 22, 33, 44, 55, 66, 77]
print(list1[-5:-3]) # [66, 77]
print(list1[6:-2])  # [77, 88]





