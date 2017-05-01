# 함수에 기본 인수 값을 지정하여 정의했습니다.
def line(char='*',count=80): print(char * count)

# 1개만 만들고 다양한 방법으로 호출이 가능하다.
print("재미있는 파이선")
line()
print("재미있는 파이선")
line(count=50)
print("재미있는 파이선")
line(char="~")
print("재미있는 파이선")
line(50,"=")
print("재미있는 파이선")
line(">",33)
