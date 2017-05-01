import glob
import os

with open('test7.txt','w', encoding='utf-8') as f:
    for i in range(10):
        print("문자열 " + str(i+1) + "\n",end='', file=f)

print('파일 크기 :', os.path.getsize('test7.txt'))
print(open('test7.txt', 'r', encoding='utf-8').read())
print('-' * 100)

# 추가모드
with open('test7.txt','a', encoding='utf-8') as f:
    for i in range(10,20):
        print("문자열 " + str(i+1) + "\n",end='', file=f)

print('파일 크기 :', os.path.getsize('test7.txt'))
print(open('test7.txt','r',encoding='utf-8').read())
print('-'*100)
