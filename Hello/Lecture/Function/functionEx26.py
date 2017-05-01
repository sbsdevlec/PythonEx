# 재귀(Recursion)호출 함수 : 자신이 자신을 호출하는 함수
def hanoi(ndisks, startPeg=1, endPeg=3):
    if ndisks:
        hanoi(ndisks - 1, startPeg, 6 - startPeg - endPeg)
        print("{}번기둥의 {}번 원반을 {}번 기둥으로 옮김!".format(startPeg, ndisks, endPeg))
        hanoi(ndisks - 1, 6 - startPeg - endPeg, endPeg)

hanoi(ndisks=3)

def countDownUp(n):
     print(n, end=' ')
     if n==0: return
     countDownUp(n-1)
     print(n, end=' ')

print()
countDownUp(5)
print()
for i in range(1,10):
    countDownUp(i)
    print()
print()

def countUpDown(n,m):
    print(n, end=' ')
    if n==m: return
    countUpDown(n+1,m)
    print(n, end=' ')

print()
countUpDown(1,10)
print()
for i in range(1,10):
    countUpDown(1,i)
    print()