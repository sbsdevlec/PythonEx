"""
Dictionary는 "키(Key) - 값(Value)" 쌍을 요소로 갖는 컬렉션이다. 
Dictionary는 흔히 Map 이라고도 불리우는데, 키(Key)로 신속하게 값(Value)을 찾아내는 해시테이블(Hash Table) 구조를 갖는다.
파이썬에서 Dictionary는 "dict" 클래스로 구현되어 있다. 
Dictionary의 키(key)는 그 값을 변경할 수 없는 Immutable 타입이어야 하며, Dictionary 값(value)은 Immutable과 Mutable 모두 가능하다.
예를 들어, Dictionary의 키(key)로 문자열이나 Tuple은 사용될 수 있는 반면, 리스트는 키로 사용될 수 없다.
Dictionary의 요소들은 Curly Brace "{...}" 를 사용하여 컬렉션을 표현하는데, 각 요소들은 "Key:Value"" 쌍으로 되어 있으며, 요소간은 콤마로 구분한다. 
요소가 없는 빈 Dictionary는 "{}"와 같이 표현한다. 특정 요소를 찾아 읽고 쓰기 위해서는 "Dictionary변수[키]"와 같이 키를 인덱스처럼 사용한다.
"""
scores = {1: 90, 2: 85, 3: 77, 4: 66}
print(scores)
v = scores[1]   # 특정 요소 읽기
print(v)
scores[1]= 88  # 쓰기
print(scores[1])
print("*"*30)

"""
파이썬의 Dictionary는 생성하기 위해 위의 예제와 같이 {...} 리터럴(Literal)을 사용할 수도 있지만, 
또한 dict 클래스의 dict() 생성자를 사용할 수도 있다. 
dict() 생성자는 (아래 첫번째 예처럼) Key-Value 쌍을 갖는 Tuple 리스트를 받아들이거나 
(두번째 예처럼) dict(key=value, key=value, ...) 식의 키-값을 직접 파라미터로 지정하는 방식을 사용할 수 있다.
"""
# 1. Tuple List로부터 dict 생성
persons = [('한사람', 30), ('두사람', 35), ('세사람', 25), ('네사람', 34), ('네사람', 78)]
mydict = dict(persons)
print(mydict)

age = mydict["두사람"]
print(age)  # 35
print("*"*30)

# 2. Key=Value 파라미터로부터 dict 생성
scores = dict(a=97, b=88, c=85)
print(scores)
print(scores['b'])
print("*"*30)

dataMap = {1:('한사람',32),2:('두사람',22)}
print(type(dataMap))
print(dataMap)
print(dataMap[2])
print(type(dataMap[2]))
print("*"*30)

dataMap2 = {1:[1,2,3,4,5],2:[11,22,33],3:[100,200,300]}
print(type(dataMap2))
print(dataMap2)
print(dataMap2[2])
print(type(dataMap2[2]))
print("*"*30)

dataMap3 = {"이름":"한사람","나이":34,"점수":[78,65,89],"취미":("술","춤","노래")}
print(type(dataMap3))
print(dataMap3)
print(dataMap3["취미"])
print(type(dataMap3["취미"]))
