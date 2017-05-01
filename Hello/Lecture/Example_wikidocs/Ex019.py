"""
019 문자열 곱하기
변수가 다음과 같이 문자열을 바인딩하고 있을 때 실행 예와 같이 출력하는 프로그램을 작성하라.
t1 = 'python'
t2 = 'java'
실행 예:
python java python java python java python java
python java java python java java
"""
t1 = 'python'
t2 = 'java'

print( (t1 + " " + t2 + " ") * 4)
print( (t1 + " " + (t2 + " ") * 2 + " ") * 2)