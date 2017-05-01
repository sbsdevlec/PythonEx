import os
# os.path 내의 파일과 디렉토리 구조 분리해 보기
path = r"c:\windows\system32\write.exe"
print(os.path.split(path))
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.splitext(path))
print(os.path.splitdrive(path))

print(os.sep)
print(os.path.join('tmp','data',os.path.basename(path)))
