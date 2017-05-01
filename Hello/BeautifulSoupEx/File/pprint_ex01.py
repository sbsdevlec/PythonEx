"""
정확히 쓰자면 'Data Pretty Print' 이다. Python에 기본적으로 포함되어 있는 pprint 모듈에 대해 간단히 소개하고자 한다.
pprint는 말 그대로 Pretty Print 이긴 한데 이름 만으론 잘 감이 안 올 수도 있다. 
이 모듈은 복잡한 자료구조의 내용을 조금 더 알기 쉽게 표시해 주는 역활이다.
"""
import pprint
tuple_data = (1,2,3,4,5)
print(tuple_data)
pprint.pprint(tuple_data)
print()

list_data = [1,2,3,4,5]
print(list_data)
pprint.pprint(list_data)
print()

dict_data = { 'result': True, 'records': [ { 'id': 1, 'value': 'First Value' }, { 'id': 2, 'value': 'Second Value' } ], 'count': 2}
print(dict_data)
pprint.pprint(dict_data)
print()

l = pprint.pformat(dict_data)
print(l)
print()

