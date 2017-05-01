# 사칙연산 함수
def add(x, y): return x + y  # 더하기
def sub(x, y): return x - y  # 빼기
def mul(x, y): return x * y  # 곱하기
def div(x, y): return x / y  # 나누기
# 전달된 함수를 실행하는 함수
def calc(fn):
    print("-"*20)
    print(x, ('','+','-','*','/')[op], y, '=', fn(x, y))  # 함수 실행
    print("-"*20)

x = int(input('첫번째 숫자를 넣어주세요'))
y = int(input('두번째 숫자를 넣어주세요'))
print("1. 더하기   2. 빼기    3. 곱하기    4. 나누기")
op = int(input('원하는 번호는?'))

fn = [add,sub,mul,div] # 함수를 리스트로 저장
if op>=1 and op<=4:
    calc(fn[op-1]) # 함수를 인수로 전달
else:
    print('지원하지 않는 연산입니다.')

