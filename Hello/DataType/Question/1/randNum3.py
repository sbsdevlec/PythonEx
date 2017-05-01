# 1~100사이의 숫자를 멸번에 맞출까요?
print("1~100사이의 정수를 생각하세요")
print("제가 몇번만에 맞출까요? 7번 이내에 맞춰볼께요....")
print('준비가 되면 엔터키를 누르세요')
count=0
min=1
max=100
input()
print("그럼 시작합니다.")
print("*" * 40)
while True:
    count += 1
    mid = (max+min)//2
    #print(max, mid, min)
    answer = input(str(mid) + '입니까(y/n)?')
    if answer.upper()=='Y':
        print('성공')
        break
    answer = input(str(mid) + "보다 큽니까(y/n)?")
    if answer.lower()=='y':
        print('크다')
        min = mid+1
    else:
        print('작다')
        max = mid-1

print("당신이 생각한 숫자는 ", mid, "입니다.", sep="")
print(str(count) + "번 만에 맞추었습니다.")
