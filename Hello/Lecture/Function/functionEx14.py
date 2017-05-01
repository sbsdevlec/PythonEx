# n의 절대값을 구하는 함수
def abs1(n):
    return n if n>0 else -n

def abs2(n):
    if n>0 :
        return n
    else:
        return -n

def abs3(n):
    if n<0 : n *= -1
    return n

n = 10;
print(n, "절대 값 :", abs1(n))
print(n, "절대 값 :", abs2(n))
print(n, "절대 값 :", abs3(n))
n = -10;
print(n, "절대 값 :", abs1(n))
print(n, "절대 값 :", abs2(n))
print(n, "절대 값 :", abs3(n))

