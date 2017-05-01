import random
print("-"*30)
print("숫자야구게임을 시작합니다 !!!")
print("-"*30)

# 컴퓨터
computer  = "".join(str(x) for x in random.sample(range(0,10),3))

totalCount=0
strikeCount = 0
while strikeCount<3:
    strikeCount = 0
    ballsCount = 0
    human = str(input("3자리 숫자를 입력하시오"))
    for c in range(0,len(computer)):
        for h in range(0,len(human)):
            if computer[c]==human[h] and c==h:
                strikeCount += 1
            elif computer[c]==human[h] and c!=h:
                ballsCount += 1
    print('Strike :' , strikeCount , ", Balls : ", ballsCount)
    totalCount += 1
print("-"*30)
print(totalCount,"번째 성공!!!", sep="")
