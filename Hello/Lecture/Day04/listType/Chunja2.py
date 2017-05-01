# 1줄씩 읽기
#file = open("chunja.txt") # UnicodeDecodeError: 'cp949' codec can't decode byte 0xa9 in position 4: illegal multibyte sequence

import codecs

file = codecs.open( "chunja2.txt", "r", "utf-8" )
chunjaList = []
print(type(chunjaList))
print(len(chunjaList))
print(chunjaList)

for i in file.readlines():
    t = i.split("|")
    chunjaList.append(t[1] + "(" + t[2] + ")")

print(len(chunjaList))
print(chunjaList)

# 찾기
if '天地玄黃(천지현황)' in chunjaList:
    index = chunjaList.index('天地玄黃(천지현황)' )
    print(chunjaList[index])
else:
    print("天地玄黃(천지현황) 없다")

def findList(list,str):
    for t in list:
        if t[0:len(str)]==str:
            return True
    return False

# 찾기
if findList(chunjaList,'天地'):
    print("있다")
else:
    print("없다")

def findList2(list,str):
    for t in list:
        if t[0:len(str)]==str:
            return t
    return ""

# 찾기
print(findList2(chunjaList,"天地"))
print(findList2(chunjaList,"宇宙洪荒"))
print(findList2(chunjaList,"추수동장"))
