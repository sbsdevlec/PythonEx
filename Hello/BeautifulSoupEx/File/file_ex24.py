import sys
import os
import array

# byte 파일을 생성 후에 읽기
# array.array(typecode[, initializer])
nums = array.array('i',[1,2,3,4,5,6])
print(type(nums))
print(nums)

with open('data.bin','wb') as f:
    f.write(nums)

with open('data.bin','rb') as f:
    print(f.read())

with open('data.bin','rb') as f:
    print(f.read().decode())

b =  array.array('i',[0,0,0,0,0,0,0,0,0,0])
with open('data.bin','rb') as f:
    f.readinto(b)
print(b)

nums[1]=11
nums[3]=33

c = array.array('i',nums);
print(id(c),c)
print(id(nums),nums)
with open('data.bin','rb') as f:
    f.readinto(c)
print(nums)
print(c)
