"""
리스트와 튜플
zip은 두 개나 그 이상의 시퀀스를 받아들여서 튜플들의 리스트로 “집(zip)” 하는데, 
각 튜플은 각 시퀀스들로부터 요소를 하나씩 받아 만들어집니다. 
파이썬 3에서, zip은 튜플의 이터레이터(iterator)를 돌려줍니다만, 대부분의 목적에서 이터레이터는 리스트처럼 동작합니다.
이 예는 문자열과 리스트를 zip 합니다:
"""
s = 'abc'
t = [0, 1, 2]
t1 = zip(s, t)
print(type(t1))
for key, value in t1:
    print(key, value)
print()

t2 = zip('Anne', 'Elk')
for key, value in t2:
    print(key, value)

