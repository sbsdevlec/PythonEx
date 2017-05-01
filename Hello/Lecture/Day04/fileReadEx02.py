import codecs
# f = open("test_utf8.txt", 'r') # UnicodeDecodeError: 'cp949' codec can't decode byte 0xeb in position 14: illegal multibyte sequence
f = codecs.open("test_utf8.txt", "r", "utf-8")
for line in f.readlines():
    print(line.replace("\n",""))

    