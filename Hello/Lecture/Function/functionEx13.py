# 1부터 n까지 합을 구하는 함수
def sum(n):
    s = 0
    while n>0:
        s += n
        n -= 1
    return s

print( 1+2+3 + 1+2+3+4+5 + 1+2+3+4+5+6+7+8+9+10)
print( sum(3) + sum(5) + sum(10))