import os
# os 명령어를 실행하고 결과 받기

f = os.popen('ipconfig')
print(f.read())

f = os.popen('dir')
print(f.read())

f = os.popen('python -V')
print(f.read())

f = os.popen('python --version')
print(f.read())

import sys
print(sys.version)

import platform
print(platform.python_version())
