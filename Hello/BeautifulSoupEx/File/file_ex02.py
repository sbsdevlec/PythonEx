import glob
import os

# 파일을 open하면 iterable 객체인 핸들을 제공
file = open('test.txt','w')

for i in range(5):
    file.write('문자열 ' + str(i+1) + '\n')
file.close()

print(os.path.getsize('test.txt'))

file = open('test.txt','r')

try:
    for i in range(10):
        print(i+1, " : ", next(file), end='')
except StopIteration:
    print('모두읽었습니다.')
file.close()
print()

for i in open('test.txt','r'):
    print(i, end='')
