# 전달된 연산자에 따라 맞는 함수를 리턴하는 함수
def calc(operator):
    def add(x,y): return x+y # 더하기
    def sub(x,y): return x-y # 빼기
    def mul(x,y): return x*y # 곱하기
    def div(x,y): return x/y # 나누기
    fn = None # 리턴할 변수
    if operator=='+': fn = add # 연산자에 따라 함수 대입
    if operator=='-': fn = sub
    if operator=='*': fn = mul
    if operator=='/': fn = div
    return fn # 함수 리턴

x = int(input('숫자를 넣어주세요'))
op = input('연산자를 넣어주세요(+,-,*,/)')
y = int(input('숫자를 넣어주세요'))

fn = calc(op) # 함수 받기

if fn is not None:
    print( x, op, y, '=',fn(x,y)) # 함수 실행
else:
    print(op + '는 지원하지 않는 연산자입니다.')
