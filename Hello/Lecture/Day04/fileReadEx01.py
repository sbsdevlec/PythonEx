f = open("test_euckr.txt", 'r')
print(f.readline())
print(f.readline())
print(f.readline().replace("\n",""))
print(f.readline().replace("\n",""))

for line in f.readlines():
    print(line.replace("\n",""))

