import pickle
import pprint
# pprint모둘은 리스트를 보기좋게 출력해준다
# pickle은 파이선 객체를 bytes타입으로 직렬화를 처리하는 모듈
data = [
    {'name':'한사람', 'age':27},
    {'name':'두사람', 'age':33},
    {'name':'세사람', 'age':18}
]

print(data)
pprint.pprint(data)

data_string = pickle.dumps(data)
print("pickle : ", data_string)

load_string = pickle._loads(data_string)
print('읽기 : ', load_string)

