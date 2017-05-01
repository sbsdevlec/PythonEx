def varArgs(message, *params):
    print(message, end='(')
    print(type(params), end=') : ')
    print(params)

varArgs("2개",3,4)
varArgs("8개",3,4,5,6,7,8,9,10)
l = [1,2,3,4,5,6,7,8,9,10]
varArgs("리스트",*l) # 리스트를 보낼때는 *을 붙입니다.
varArgs("리스트",l) # 리스트를 보낼때는 *을 붙이지 않으면
t = (1,2,3,4,5,6,7,8,9,0)
varArgs("튜플",*t) # tuple을 보낼때도 *을 붙입니다.
varArgs("튜플",t) # tuple을 보낼때 *을 붙이지 않으면

"""
한 가지 주의할 점은 일반 인자와 가변 인자가 동시에 오는 경우
반드시 가변 인자는 일반 인자 뒤에 와야 한다는 점이다. 
또한 가변 인자는 단 하나만 사용할 수 있다는 것도 유의해야 한다.
"""