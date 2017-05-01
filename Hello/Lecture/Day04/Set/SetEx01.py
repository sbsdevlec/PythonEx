"""
Set은 중복이 없는 요소들 (unique elements)로만 구성된 집합 컬렉션이다.
 Set은 Curly Brace { } 를 사용하여 컬렉션을 표현하는데, 내부적으로 요소들을 순서대로 저장하기 않기 때문에, 
 순서에 의존하는 기능들을 사용할 수 없다. 만약 set을 정의할 때, 중복된 값을 입력하는 경우, set은 중복된 값을 한번만 가지고 있게 된다. 
리스트나 튜플 등을 set으로 변경하기 위해서는 set() 생성자를 사용한다. 이는 리스트에 중복된 값들이 있을 때, 중복 없이 Unique한 값만을 얻고자 할 때 유용하다.
"""
myset = {1,1,1,2,2,2,3,3,3}
print(myset)

mylist = [1,1,1,2,2,2,3,3,3]
print(mylist)
myset = set(mylist)
print(myset)

# 하나만 추가
myset.add(7)
print(myset)

# 여러 개 추가
myset.update({4, 2, 10})
print(myset)

# 하나만 삭제
myset.remove(1)
print(myset)

# 모두 삭제
myset.clear()
print(myset)