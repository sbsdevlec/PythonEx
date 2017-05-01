import codecs

file = codecs.open("test_utf8.txt", "w", "utf-8")
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    file.write(data)
file.close()
