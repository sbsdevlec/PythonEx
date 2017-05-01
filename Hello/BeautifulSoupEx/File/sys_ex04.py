import sys
# sys.byteorder
print(sys.byteorder)
print(sys.maxsize)
print(sys.maxunicode)

for key in sys.modules:
    print(key, ' : ', sys.modules[key])
print()

for p in sys.path:
    print(p)
