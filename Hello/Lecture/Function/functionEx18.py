import random # 난수 사용

def desc(list):
    return sorted(list,reverse=True)

def asc(list):
    return sorted(list)

def mySort(fn,list): # 함수를 인수로 받음
    print("오름차순 정렬 : " if  fn==asc else "내림차순 정렬 : ", end='')
    print(fn(list))

list = random.sample(range(1,101),10)
print("원본 :",list)
mySort(desc,list)
mySort(asc,list)
print()

list2 = ["한사람","두사람","세사람","네사람","오사람"]
print("원본 :",list2)
mySort(desc,list2)
mySort(asc,list2)
