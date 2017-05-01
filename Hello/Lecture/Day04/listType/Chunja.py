import codecs

file = codecs.open( "chunja.txt", "r", "utf-8" )
chunjaList = []
print(type(chunjaList))
print(len(chunjaList))
print(chunjaList)

for i in file.readlines():
    t = i.split("|")
    chunjaList.append(t[1] + "(" + t[2] + "," + t[3].replace("\r\n","") + ")")

print(len(chunjaList))
print(chunjaList)

# 찾기
if '天(천,하늘 천)' in chunjaList:
    index = chunjaList.index('天(천,하늘 천)' )
    print(chunjaList[index])
else:
    print("天(천,하늘 천) 없다")


