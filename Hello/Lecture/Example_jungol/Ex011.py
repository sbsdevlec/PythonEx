"""
국어,영어,수학,전산 점수를 입력받아
다음과 같이 출력되는 프로그램을 작성하시오.
합계와 평균은 수식을 이용하세요. 
국어 : 57
영어 : 64
수학 : 78
전산 : 91
합계 :  290
평균 :  72.5
"""
kor = int(input("국어 : "))
eng = int(input("영어 : "))
mat = int(input("수학 : "))
edps = int(input("전산 : "))
tot = kor + eng + mat + edps
avg = tot/4.0
print("합계 : ", tot)
print("평균 : ", avg)