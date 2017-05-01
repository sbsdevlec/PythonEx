import random
# 컴퓨터
computer = random.sample(range(0,10),3)
# print("컴퓨터 발생숫자 : ", computer)

#사람
print("-"*30)
print("숫자야구게임을 시작합니다 !!!")
print("-"*30)
human = str(input("3자리 숫자를 입력하시오"))

# 임시출력
print("컴퓨터 발생숫자 : ", computer)
print("사람 입력숫자 : ", human)
