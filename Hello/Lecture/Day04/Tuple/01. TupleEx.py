"""
튜플(tuple)은 몇 가지 점을 제외하곤 리스트와 거의 비슷하며 리스트와 다른 점은 다음과 같다.
리스트는 [과 ]으로 둘러싸지만 튜플은 (과 )으로 둘러싼다.
리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.
"""

tuple1 = ()
print(tuple1)
tuple2 = (1)
print(tuple2, type(tuple2))
tuple3 = (1,)
print(tuple3, type(tuple3))
tuple4 = (1,2,3,4,5)
print(tuple4)
tuple5 = 1,2,3,4,5
print(tuple5)
tuple6 = ('a', 'b', ('1', '2','3'),(1,2,3))
print(tuple6)
"""
리스트와 모습은 거의 비슷하지만 튜플에서는 리스트와 다른 2가지 차이점을 찾아볼 수 있다. 
t2 = (1,)처럼 단지 1개의 요소만을 가질 때는 요소 뒤에 콤마(,)를 반드시 붙여야 한다는 것과 
t4 = 1, 2, 3처럼 괄호()를 생략해도 무방하다는 점이다.
얼핏 보면 튜플과 리스트는 비슷한 역할을 하지만 프로그래밍을 할 때 튜플과 리스트는 구분해서 사용하는 것이 유리하다. 
튜플과 리스트의 가장 큰 차이는 값을 변화시킬 수 있는가 없는가이다.
즉, 리스트의 항목값은 변화가 가능하고 튜플의 항목값은 변화가 불가능하다. 
따라서 프로그램이 실행되는 동안 그 값이 항상 변하지 않기를 바란다거나 값이 바뀔까 걱정하고싶지 않다면 
주저하지 말고 튜플을 사용해야 한다. 이와는 반대로 수시로 그 값을 변화시켜야할 경우라면 리스트를 사용해야 한다. 
실제 프로그램에서는 값이 변경되는 형태의 변수가 훨씬 많기 때문에 평균적으로 튜플보다는 리스트를 더 많이 사용하게 된다.
"""
print(tuple6[0], type(tuple6[0]))
print(tuple6[1], type(tuple6[1]))
print(tuple6[2], type(tuple6[2]))
print(tuple6[3], type(tuple6[3]))

# 튜플 요소값 삭제 시 오류
# del tuple6[0]
'''
Traceback (most recent call last):
  File "C:/Users/DJA/PycharmProjects/Lecture/Day03/Tuple/01. TupleEx.py", line 36, in <module>
    del tuple6[0]
TypeError: 'tuple' object doesn't support item deletion
'''

# 튜플 요소값 변경 시 오류
tuple6[0] = 'qwerty'
'''
Traceback (most recent call last):
()
  File "C:/Users/DJA/PycharmProjects/Lecture/Day03/Tuple/01. TupleEx.py", line 45, in <module>
1 <class 'int'>
    tuple6[0] = 'qwerty'
(1,) <class 'tuple'>
TypeError: 'tuple' object does not support item assignment
'''
