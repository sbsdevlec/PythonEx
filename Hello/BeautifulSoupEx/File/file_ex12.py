import glob
import os

with open('test10.txt','w', encoding='utf-8') as f:
    print("12345\n",end='', file=f)
    print("1234567890\n",end='', file=f)

print('파일 크기 :', os.path.getsize('test10.txt'))
print(open('test10.txt', 'r', encoding='utf-8').read())
print('-' * 100)

file = open('test10.txt','a+', encoding='utf-8')
file.write('*********\n')
file.write('추가된내용\n')
file.seek(0)
print(file.read())
print('-' * 100)
file.close()

print('파일 크기 :', os.path.getsize('test10.txt'))
print(open('test10.txt', 'r', encoding='utf-8').read())
print('-' * 100)
