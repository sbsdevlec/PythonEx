# 1줄씩 읽기
#file = open("chunja.txt") # UnicodeDecodeError: 'cp949' codec can't decode byte 0xa9 in position 4: illegal multibyte sequence

import codecs

file = codecs.open( "chunja2.txt", "r", "utf-8" )
for i in file.readlines():
    t = i.split("|")
    print(t[1]+"["+t[2]+"] : " + t[3])

file = codecs.open( "chunja2.txt", "r", "utf-8" )
chunjaDict = {}
print(type(chunjaDict))
print(chunjaDict)
for i in file.readlines():
    t = i.split("|")
    chunjaDict[t[0]]=t[1]+"["+t[2]+"] : " + t[3] + " : " + t[4].replace("\r\n","")

print(chunjaDict)

for key in chunjaDict.keys():
    print(key + " : " + chunjaDict[key])

# 찾기
if '200' in chunjaDict.keys():
    print(chunjaDict['200'])
else:
    print("200은 없다")

if '1000' in chunjaDict.keys():
    print(chunjaDict['1001'])
else:
    print("1000은 없다")