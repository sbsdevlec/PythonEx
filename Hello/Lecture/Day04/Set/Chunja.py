import codecs

file = codecs.open( "chunja.txt", "r", "utf-8" )
chunjaSet = set()
print(type(chunjaSet))
print(len(chunjaSet))
print(chunjaSet)

for i in file.readlines():
    t = i.split("|")
    chunjaSet.add(t[0] +". "  + t[1] + "(" + t[2] + ") : " + t[3].replace("\r\n",""))

print(len(chunjaSet))
print(chunjaSet)


