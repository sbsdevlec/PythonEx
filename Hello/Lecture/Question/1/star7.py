height = int(input("몇줄짜리?"))
str=""
len = 0
# 파이선 삼항연산!!!!
# 참 if 조건 else 거짓
for i in range(1,height*2) :
    len += 1 if i<=height else -1
    str += "  " * (height - len) + "☆" * (len * 2 - 1) + "\n"
print(str)


