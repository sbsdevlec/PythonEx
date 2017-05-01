# 1줄씩 읽기
#file = open("chunja.txt") # UnicodeDecodeError: 'cp949' codec can't decode byte 0xa9 in position 4: illegal multibyte sequence

import codecs

file = codecs.open( "chunja.txt", "r", "utf-8" )
print(file.readline(), end="")
print(file.readline(), end="")

for i in file.readlines():
    print(i, end="" )

chunjaDict={}
file = codecs.open( "chunja.txt", "r", "utf-8" )
for i in file.readlines():
    t = i.split("|")
    print(t[0] + " : " + t[1] + "(" + t[2] + "," + t[3].replace("\r\n","") + ")")
    chunjaDict[t[0]] = t[1] + "(" + t[2] + "," + t[3].replace("\r\n","") + ")"

print(chunjaDict)
for key in chunjaDict.keys():
    print(key +":" + chunjaDict[key])


# 찾기
if '1000' in chunjaDict.keys():
    print(chunjaDict['1000'])
else:
    print("1000은 없다")

if '1001' in chunjaDict.keys():
    print(chunjaDict['1001'])
else:
    print("1001은 없다")