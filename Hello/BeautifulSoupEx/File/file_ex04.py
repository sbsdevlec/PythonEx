import glob
import os
# file.tell() : 현재 파일 포인터의 위치를 알려줌
file = open('test2.txt','w')

for i in range(5): file.write(str(i+1) + ' : 문자열 1234567890\n')
file.close()
print('파일 크기 :', os.path.getsize('test2.txt'))

file = open('test2.txt','r')
print("현재 파일 포인터 :", file.tell())
print(file.readline()[:-1]) # 엔터 주의
print("현재 파일 포인터 :", file.tell())
print(file.read(10)) # 한글 주의
print("현재 파일 포인터 :", file.tell())
print('-'*100)
file.close()
