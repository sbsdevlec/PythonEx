# 1~100사이의 숫자를 몇번에 맞출까요?
import random

computer = random.randint(1,101)
num=0
count=0
while (num!=computer):
    num = int(input("1~100 사이의 숫자를 입력하세요?"))
    count += 1
    if num<computer:
        print("입력한 값이 작아요!!!")
    elif num>computer:
        print("입력한 값이 커요!!!")
print("-"*50)
print(count,"번째 마추셨습니다.",sep=" ")

