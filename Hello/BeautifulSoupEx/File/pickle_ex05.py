import pickle
import pprint
# 클래스 저장 및 로딩
class Fruits:
    pass

banana = Fruits()
banana.color = 'yellow'
banana.value = 44
apple = Fruits()
apple.color = 'red'
apple.value = 55


file_obj1 = open('pickle.class','wb')
pickle.dump(banana,file_obj1)
pickle.dump(apple,file_obj1)
file_obj1.close()


file_obj2 = open('pickle.class','rb')
object_banana = pickle.load(file_obj2)
object_apple = pickle.load(file_obj2)
print(object_banana)
print(object_banana.color, object_banana.value)
print(object_apple)
print(object_apple.color, object_apple.value)
