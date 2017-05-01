import glob
import os
from fnmatch import fnmatch
"""
glob() 함수는 경로에 대응되는 모든 파일 및 디렉터리의 리스트를 반환합니다.
'*'와 '?'도 사용가능하며 "["과"]"를 사용한 문자열 비교도 가능합니다.
"""
files = glob.glob("*")
print(files)
print()

files = glob.glob("./[a-g]*.*")
print(files)
print()

files = glob.glob("*.py")
print(files)
print()

files = glob.glob("????_*.*")
print(files)
print()

files = glob.glob(os.path.abspath('.' + '\\*.py'))
print(files)
print()

print(os.listdir('.'))
print()

pyfiles = [name for name in os.listdir('.') if fnmatch(name,'*.py')]
print(pyfiles)
print()

# glob과 동일한 동작을 수행하지만, 리스트로 결과를 반환하는 것이 아니라 이터레이터를 반환.
# 한번에 모든 결과를 리스트에 담지 않으므로, 결과가 매우 많은 경우 유용하게 쓰일 수 있다.
print(glob.iglob('*'))
for i in glob.iglob('*'):
    print (i)
print()

for i in glob.glob("./*"):
    print(i)

