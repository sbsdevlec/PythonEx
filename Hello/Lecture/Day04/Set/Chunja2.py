# 1줄씩 읽기
#file = open("chunja.txt") # UnicodeDecodeError: 'cp949' codec can't decode byte 0xa9 in position 4: illegal multibyte sequence

import codecs

file = codecs.open( "chunja2.txt", "r", "utf-8" )

chunjaSet = set()
print(type(chunjaSet))
print(len(chunjaSet))
print(chunjaSet)

for i in file.readlines():
    t = i.split("|")
    chunjaSet.add(t[0] +". "  + t[1] + "(" + t[2] + ") : " + t[4].replace("\r\n",""))

print(len(chunjaSet))
print(chunjaSet)

