# 변환
class Data(object):
    def __str__(self):
        return 'str한글'
    def __repr__(self):
        return 'repr한글'

print("{} {}".format(Data(),Data()))
print("{!a} {!r}".format(Data(),Data()))
print("{!s} {!r}".format(Data(),Data()))