"""
튜플(tuple)은 몇 가지 점을 제외하곤 리스트와 거의 비슷하며 리스트와 다른 점은 다음과 같다.
리스트는 [과 ]으로 둘러싸지만 튜플은 (과 )으로 둘러싼다.
리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.
"""

#  list to tuple
list1  = [1,2,3,4,5]
print(list1, type(list1))
tuple1 = tuple(list1)
print(tuple1, type(tuple1))
