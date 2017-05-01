import os
import tempfile

# tempfile을 사용하면 사용이 종료되면 자동으로 삭제가 됨

# 만들고 사용하고 지우고
filename = "temp_{}.txt".format(os.getpid())
temp = open(filename,'w+b')
try:
    print('temp :', temp)
    print('temp.name :', temp.name)
finally:
    temp.close()
    os.remove(filename) # 삭제
print()

# 만들고 사용하고 자동으로 지우고
temp = tempfile.TemporaryFile()
try:
    print('temp :', temp)
    print('temp.name :', temp.name)
finally:
    temp.close()
print()

# 만들고 사용하고 자동으로 지우지 않고(보안에 문제가 됨)
#temp = tempfile.NamedTemporaryFile(delete=False, prefix='test_',suffix='_temp')
temp = tempfile.NamedTemporaryFile(delete=False)
try:
    print('temp :', temp)
    print('temp.name :', temp.name)
finally:
    temp.close()

#os.unlink(temp.name)
print(os.path.exists(temp.name))
print()

#
temp = tempfile.TemporaryFile(prefix='test_',suffix='_temp')
try:
    print('temp :', temp)
    print('temp.name :', temp.name)
finally:
    temp.close()
