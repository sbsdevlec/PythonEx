import pickle
import pprint
# 리스트 저장 및 로딩
save_list =['한놈','두식이','석삼','너구리','오징어']
print(save_list)
file_obj1 = open('pickle.list','wb')
pickle.dump(save_list,file_obj1)
file_obj1.close()


file_obj2 = open('pickle.list','rb')
load_list= pickle.load(file_obj2)
print(load_list)
print()
print(save_list == load_list)