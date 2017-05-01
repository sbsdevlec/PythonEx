"""
서식 문자를 사용하여 다음과 같이 출력되는 프로그램을 작성하라.
msg = "파이선Program"
star = "★"
출력예
나도 프로그램을 잘할 수 있다.
           꿈★은 이루어진다.
"""
msg = "파이선Program"
star = "★"

print("나도 {0}을 잘할 수 있다.".format(msg))
print("     꿈{0}은 이루어진다.".format(star))
print()
print("나도 {0}을 잘할 수 있다.".format(msg))
print(" " * len(msg) + "      꿈{0}은 이루어진다.".format(star))
print()
print("나도 %s을 잘할 수 있다."%(msg))
print(" " * len(msg) + "      꿈%s은 이루어진다."%(star))
