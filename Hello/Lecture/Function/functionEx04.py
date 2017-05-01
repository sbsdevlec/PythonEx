def showMessage(char, count=3):
	'''
	문자열과 숫자를 받고 문자열을 지정 숫자만큼 출력하는 함수
	'''
	print(char*count)

showMessage('짝')
showMessage('짝',5)
showMessage(7, '짝')

# 아래와 같이 출력해도 된다. 스스로 타입을 인식하여 대입을 받는다.
showMessage(count=10,char='짝')
showMessage(char='짝',count=20)
showMessage('짝',count=30)
showMessage(30) # 30을 string이 받음 그리고 count가 3이됨 결과는 90
# clap(count=30) # Error :
#  기본값이 없는 인수가 1개있으므로 반드시 기본값이 없는 char가 없으면 Error!!!!
# 반드시 1개의 인수는 있어야 합니다.
print()
