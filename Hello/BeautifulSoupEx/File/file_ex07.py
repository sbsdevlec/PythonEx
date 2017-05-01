import glob
import os

strings = '''문자열 1
문자열 2
문자열 3
문자열 4
문자열 5
'''
file = open('test5.txt','w', encoding='utf-8')
file.writelines(strings)
file.close()

print('파일 크기 :', os.path.getsize('test5.txt'))
print(open('test5.txt','r',encoding='utf-8').read())
print('-'*100)