import pickle
import pprint
# dict 저장 및 로딩
save_dict = [
    {'name':'한사람', 'age':27},
    {'name':'두사람', 'age':33},
    {'name':'세사람', 'age':18}
]
print(save_dict)
file_obj1 = open('pickle.dict','wb')
pickle.dump(save_dict,file_obj1)
file_obj1.close()


file_obj2 = open('pickle.dict','rb')
load_dict= pickle.load(file_obj2)
print(load_dict)
print()
print(save_dict == load_dict)