import glob
import os
# file.seek() : 현재 파일 포인터의 위치를 변경합
file = open('test4.txt','w')
for i in range(5):
    file.write(str(i+1) + ' : 1234567890\n')
file.close()
print('파일 크기 :', os.path.getsize('test4.txt'))
print(open('test4.txt','r').read())
print('-'*100)

# 자동 닫기
with open('test4.txt','r') as file:
    print(file.closed)
    print(file.readline()[:-1])
    print(file.read(10))
print()
print(file.closed)
