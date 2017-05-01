class Monster:
    __count = 0
    # 초기자(initializer) 또는 생성자(Constructor)
    def __init__(self):
        Monster.__count += 1
    # 소멸자(Destructor)
    def __del__(self):
        Monster.__count -= 1

    # 정적 메서드
    @staticmethod
    def getCount():
        return Monster.__count

print(Monster.getCount(),  "마리");
m1 = Monster()
print(Monster.getCount(),  "마리");
m2 = Monster()
print(Monster.getCount(), "마리");
m3 = Monster()
print(Monster.getCount(), "마리");
del m3, m2
print(Monster.getCount(), "마리");
if Monster.getCount()==0:
    print("모든 몬스터를 잡아서 게임을 종료합니다.")
else:
    print("아직 잡아야할 몬스터가 " + str(Monster.getCount()) + "마리 더있습니다.")

#print(Monster.__count) # AttributeError: type object 'Monster' has no attribute '__count'

del m1
print(Monster.getCount(), "마리");
if Monster.getCount()==0:
    print("모든 몬스터를 잡아서 게임을 종료합니다.")
else:
    print("아직 잡아야할 몬스터가 " + str(Monster.getCount()) + "마리 더있습니다.")
