import glob
import os

# 파일을 open하면 iterable 객체인 핸들을 제공
file = open('test1.txt','w')
for line in range(10):
    for i in range(10):
        file.write(str(i))
    file.write("\n")
file.close()

print(os.path.getsize('test1.txt'))

for i in open('test1.txt','r'):
    print(i, end='')
print("-"*100)
# 파일을 open하고 read메서드를 호출하면 모두 str 타입으로 생성됨
# 원하는 크기만 읽기
file = open('test1.txt','r')
string = file.read(5)
print(string)
string = file.read(15)
print(string)
file.close()
print("-"*100)

# 모두읽기
file = open('test1.txt','r')
string = file.read()
print(string)
print("-"*100)

# 1줄읽기
file = open('test1.txt','r')
string = file.readline()
print(string)
string = file.readline()
print(string, end='')
string = file.readline()[:-1]
print(string)
print("-"*100)

# readlines()로 읽기
file = open('test1.txt','r')
for line in file.readlines():
    print(line[:-1])
print("-"*100)
