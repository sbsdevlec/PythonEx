# 파일 열기모드 x : 파일이 없을 때만 생성 있으면 예외
filename = 'c:\\temp\\somefile.txt'
try:
    with open(filename, 'xt') as f:
        f.write('하하하하\n')
        f.close()
        print(filename + '을 만들었습니다.')
except  FileExistsError:
    print(filename + '은 이미 존재합니다. 내용을 추가합니다.')
    with open(filename, 'a') as f:
        f.write('추가된 내용입니다.\n')
        f.close()

f = open(filename,'r')
print('파일내용\n========')
print(f.read())