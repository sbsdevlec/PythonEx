import os

# 파일 열기모드 x : 파일이 없을 때만 생성 있으면 예외
filename = 'c:\\temp\\somefile1.txt'
if  os.path.exists(filename):
    print(filename + '은 이미 존재합니다. 내용을 추가합니다.')
    with open(filename, 'a') as f:
        f.write('추가된 내용입니다.\n')
        f.close()
else:
    with open(filename, 'w') as f:
        f.write('처음으로 만듭니다.\n')
        f.close()
        print(filename + '을 만들었습니다.')

f = open(filename,'r')
print('파일내용\n========')
print(f.read())