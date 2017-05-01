# 재귀(Recursion)호출 함수 : 자신이 자신을 호출하는 함수
def sum(n):
    return 0 if n <= 0 else n + sum(n - 1)

for i in range(1,11):
    print("1에서 {}까지 합 : {}".format(i, sum(i)))
print()

def factorial(n):
    return 1 if n<1 else n * factorial(n-1)

for i in range(1,11):
    print(i,"!=", factorial(i))
print()

def rangeSum(n,m):
    return n if n==m else n + rangeSum(n+1,m)

print(rangeSum(1,10))
print(rangeSum(11,20))
print()

def rangeSum2(n,m):
    if n>m: m, n = n, m
    return n if n==m else n + rangeSum(n+1,m)

print(rangeSum2(1,10))
print(rangeSum2(10,1))
print()

def rangeSum3(n,m):
    if n>m: m, n = n, m
    return rangeSum(n,m)

print(rangeSum3(1,10))
print(rangeSum3(10,1))
print()

def fibonacci(n):
    return 1 if n==1 or n==2 else fibonacci(n-1)+fibonacci(n-2)

for i in range(1,11):
    print(fibonacci(i), end=' ')
print()

# 재귀호출이 안좋은 예~~~~ 반복 호출이 많다.
def fibonacci2(n):
    print("fibonacci2({})호출!".format(n))
    return 1 if n==1 or n==2 else fibonacci2(n-1)+fibonacci2(n-2)

fibonacci2(5)