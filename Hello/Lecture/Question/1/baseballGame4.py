import random
# 컴퓨터
computer  = "".join(str(x) for x in random.sample(range(0,10),3))
# print("컴퓨터 발생숫자 : ", computer)

#사람
print("-"*30)
print("숫자야구게임을 시작합니다 !!!")
print("-"*30)
human = str(input("3자리 숫자를 입력하시오"))

# 임시출력
print("컴퓨터 발생숫자 : ", computer)
print("사람   입력숫자 : ", human)
strikeCount = 0
ballsCount = 0

# for c in range(0,3):
#     for h in range(0,3):
#         print(computer(c), human(h))
#     print('*'*10)

# for c in range(0,len(computer)):
#     for h in range(0,len(human)):
#         print(computer[c], human[h])
#     print('*'*10)

for c in range(0,len(computer)):
    for h in range(0,len(human)):
        if computer[c]==human[h] and c==h:
            strikeCount +=1
        elif computer[c]==human[h] and c!=h:
            ballsCount +=1

print('Strike :' , strikeCount , ", Balls : ", ballsCount)