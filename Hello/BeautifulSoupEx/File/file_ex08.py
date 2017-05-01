import glob
import os

with open('test6.txt','w', encoding='utf-8') as f:
    for i in range(10):
        print("문자열 " + str(i+1) + "\n",end='', file=f)

print('파일 크기 :', os.path.getsize('test6.txt'))
print(open('test6.txt','r',encoding='utf-8').read())
print('-'*100)

with open('test6.txt','rt', encoding='utf-8') as f:
    for line in f:
        print(line,end='')
print('-'*100)


