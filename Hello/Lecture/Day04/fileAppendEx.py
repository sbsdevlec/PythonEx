import codecs

file = codecs.open("test_utf8.txt", "r", "utf-8")
for i in file.readlines():
    print(i)
file.close()

file = codecs.open("test_utf8.txt", "a", "utf-8")
for i in range(11, 21):
    data = "%d번째 추가된 줄입니다.\n" % i
    file.write(data)
file.close()

file = codecs.open("test_utf8.txt", "r", "utf-8")
for i in file.readlines():
    print(i)
file.close()

