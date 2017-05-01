def greet(name):
	'''
	이름을 인수로 받아 인사를 하는 함수입니다.
	'''
	print("안녕하세요 " + name + "씨 반갑습니다.")

greet('한사람')
greet('두사람')
greet('세사람')

print(greet.__doc__)
print(print.__doc__)