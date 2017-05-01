import sys
import os
import array

# byte 파일을 생성 후에 읽기
str1 = b"Hello World!!!\n"
str2 = u"안녕하세요!!!\n"
str3 = "Hello World!!! 안녕하세요!!!\n"

with open('data2.bin','wb') as f:
    f.write(str1)
    f.write(str2.encode())
    f.write(str3.encode())

with open('data2.bin','rb') as f:
   for line in f:
       print(line)
       print(line.decode()[:-1])

