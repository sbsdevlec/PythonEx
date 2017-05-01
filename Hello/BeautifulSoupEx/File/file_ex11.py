import glob
import os

with open('test9.txt','w', encoding='utf-8') as f:
    for i in range(10):
        print("문자열 " + str(i+1) + "\n",end='', file=f)

file1 = open('test9.txt','r', encoding='utf-8')
file2 = open('test9.bak','w', encoding='utf-8')
count = 1
for line in file1:
    #print(line.rstrip())
    file2.write(line.rstrip() + "\n")
    count += 1
file1.close()
file2.close()

print('원본 파일 크기 :', os.path.getsize('test9.txt'))
print(open('test9.txt', 'r', encoding='utf-8').read())
print('-' * 100)

print('복사 파일 크기 :', os.path.getsize('test9.bak'))
print(open('test9.bak', 'r', encoding='utf-8').read())
print('-' * 100)
