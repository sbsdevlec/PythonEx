import os
# os.path

names = os.listdir(".")
print(names)

names = os.listdir('c:\\')
print(names)

# 윈도우는 \\로 디렉토리 구분 raw스트링 처리시 \로 처리
names = os.listdir(r'c:\windows')
print(names)

names = os.listdir(u'c:\windows')
print(names)

