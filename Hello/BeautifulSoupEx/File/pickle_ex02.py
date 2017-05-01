import pickle
import pprint
# 문자열 저장 및 로딩
save_string = "이 내용을 저장할 것입니다."
print(save_string)
file_obj1 = open('pickle.pk','wb')
pickle.dump(save_string,file_obj1)
file_obj1.close()


file_obj2 = open('pickle.pk','rb')
load_string = pickle.load(file_obj2)
print(load_string)
print()
print(save_string == load_string)