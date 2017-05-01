import sys
# 명령행 인수
print(sys.argv)

for i in (sys.stdin,sys.stdout,sys.stderr):
    print(i)

print(vars(sys.stdout))
print(dir(sys.stdout))
sys.stdout.write('이름을 입력하시오')
sys.stdout.flush()
print('이름 : ', sys.stdin.readline()[:-1])
