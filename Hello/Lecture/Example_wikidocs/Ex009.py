"""
009 사칙 연산
사용자로부터 두 개의 숫자를 입력 받은 후 두 숫자의 덧셈(+), 뺄셈(-), 곱셈(*), 나눗셈(/) 결괏값을 출력하라.
실행 예:
first number : 45
second number : 103
add :  148
sub :  -58
mul :  4635
div1 :  0.4368932038834951
div2 :  0
mod :  45
"""
i = int(input("first number : "))
j = int(input("second number : "))
print("add : ", i+j)
print("sub : ", i-j)
print("mul : ", i*j)
print("div1 : ", i/j)
print("div2 : ", i//j)
print("mod : ", i%j)