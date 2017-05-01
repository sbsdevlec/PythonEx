import glob
import os
# file.seek() : 현재 파일 포인터의 위치를 변경합
file = open('test3.txt','w')

for i in range(5):
    file.write(str(i+1) + ' : 1234567890\n')
file.close()
print('파일 크기 :', os.path.getsize('test3.txt'))

print(open('test3.txt','r').read())
print('-'*100)

file = open('test3.txt','r')
print("현재 파일 포인터 :", file.tell())
print(file.readline()[:-1]) # 엔터 주의
print("현재 파일 포인터 :", file.tell())
file.seek(0)
print("현재 파일 포인터 :", file.tell())
print('-'*100)
file.close()

file = open('test3.txt','rb+')
file.seek(10)
print("현재 파일 포인터 :", file.tell())
file.seek(20)
print("현재 파일 포인터 :", file.tell())
file.seek(20,1) # 파일이 읽기 전용이면 에러. 두번째 인수가 1이면 현재위치가 기준
print("현재 파일 포인터 :", file.tell())
file.seek(-10,1)
print("현재 파일 포인터 :", file.tell())
file.seek(0,2) # 파일이 읽기 전용이면 에러. 두번째 인수가 2이면 맨뒤 위치가 기준
print("현재 파일 포인터 :", file.tell())
file.seek(-10,2)
print(file.read(10))
print("현재 파일 포인터 :", file.tell())
file.seek(10,2)
print(file.read(10))
print("현재 파일 포인터 :", file.tell())
print('-'*100)
file.close()

