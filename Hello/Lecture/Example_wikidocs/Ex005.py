"""
005 사용자 입력
사용자로부터 출력하고자 하는 문자열과 반복 횟수를 입력 받은 후 문자열을 반복 횟수만큼 출력하는 프로그램을 작성하라.
실행 예:
문자열: hello
반복횟수: 4
"hellohellohellohello"
"""
str = input("문자열 : ")
count = int(input("반복횟수 : "))
print(str * count)