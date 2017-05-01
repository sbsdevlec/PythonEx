import glob
import os

with open('test8.txt','w', encoding='utf-8') as f:
    for i in range(10):
        print("문자열 " + str(i+1) + "\n",end='', file=f)

print('파일 크기 :', os.path.getsize('test8.txt'))
print(open('test8.txt', 'r', encoding='utf-8').read())
print('-' * 100)

file = open('test8.txt','w+', encoding='utf-8')
file.truncate() # 파일의 내용을 지워버린다.
f.close()

print('파일 크기 :', os.path.getsize('test8.txt'))
print(open('test8.txt', 'r', encoding='utf-8').read())
print('-' * 100)
