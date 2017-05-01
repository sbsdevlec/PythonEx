import os
# os 내의 디렉토리 정보를 조회하거나 디렉토리 내의 정보 조회
print(os.getcwd())
print(os.path.curdir)
print(os.path.dirname(os.getcwd()))
# 디렉토리
os.chdir('..')
print(os.getcwd())
#os.mkdir('./test')
os.chdir('./test')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())

