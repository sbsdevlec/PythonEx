# 산술 연산자 : + - * / // % **
i = 10
j = 3;

print("{0} + {1} = {2}".format(i, j, i+j))
print("{0} - {1} = {2}".format(i, j, i-j))
print("{0} * {1} = {2}".format(i, j, i*j))
print("{0} / {1} = {2}".format(i, j, i/j))
print("{0} // {1} = {2}".format(i, j, i//j))
print("{0} % {1} = {2}".format(i, j, i%j))
print("{0} ** {1} = {2}".format(i, j, i**j))
print()

i = 10
j = 3.0;
print("{0} + {1} = {2}".format(i, j, i+j))
print("{0} - {1} = {2}".format(i, j, i-j))
print("{0} * {1} = {2}".format(i, j, i*j))
print("{0} / {1} = {2}".format(i, j, i/j))
print("{0} // {1} = {2}".format(i, j, i//j))
print("{0} % {1} = {2}".format(i, j, i%j))
print("{0} ** {1} = {2}".format(i, j, i**j))
print()

# 나눗셈을 연산하는 divmod() 라는 함수도 있는데,
# 몫과 나머지를 튜플로 반환한다.
print(divmod(i, j))  # (3.0, 1.0)
