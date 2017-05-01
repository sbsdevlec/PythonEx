class Person:
    name="무명"
    age=0
    def __init__(self):
        pass

Person.name = '김사람'
Person.age = 33
print( Person.name + "씨(" + str(Person.age) + "세)")

Person.name = '이주인'
Person.age = 24
print( Person.name + "씨(" + str(Person.age) + "세)")

# 다시 "김사람"을 사용할 방법이 없을까?
print( Person.name + "씨(" + str(Person.age) + "세)")
print()

kimc = Person()
kimc.name = '김사람'
kimc.age = 33
print( kimc.name + "씨(" + str(kimc.age) + "세)")
print()

saram = Person()
print( kimc.name + "씨(" + str(kimc.age) + "세)")
print( saram.name + "씨(" + str(saram.age) + "세)")
print()

hong = Person()
hong.name = '홍길녀'
hong.age = 24
hong.gender = '여'

print( kimc.name + "씨(" + str(kimc.age) + "세)")
print( hong.name + "씨(" + str(hong.age) + "세)")
print( saram.name + "씨(" + str(saram.age) + "세)")
print()

print(vars(kimc))
print(vars(hong))
print(vars(saram))
print(vars(Person))


