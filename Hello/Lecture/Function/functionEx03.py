def showMessage(message, count):
	'''
	문자열과 숫자를 받고 문자열을 지정 숫자만큼 출력하는 함수
	'''
	print(type(message))
	print(type(count))
	print(message * count)

print(showMessage.__doc__)
showMessage('짝',5)

# 아래와 같이 출력해도 된다. 스스로 타입을 인식하여 대입을 받는다.
showMessage(10,'짝')

# 아래와 같이 출력해도 된다. 스스로 타입을 인식하여 대입을 받는다.
showMessage(10,20)
print()