from collections import namedtuple
# C 언어에서 이 문화적 차이를 대입해보면 목록은 배열(array) 같고 튜플은 구조체(struct)와 비슷할 것이다.
Station = namedtuple("Station", "id, city, state, lat, long")
denver = Station(44, "Denver", "CO", 40, 105)
print(denver)
print(denver.city)
print(denver[1])

print(denver.state)
print(denver[2])
