import glob
import os
import io
# 텍스트 파일 처리( In-memory Streams )
# readline()및 readlines()메서드도 사용할 수 있습니다.
# 또한 StringIO 클래스는 seek()읽기 동안 버퍼에서 점프 하는 방법을 제공하며
# 미리 읽기 구문 분석 알고리즘이 사용되는 경우 되감기에 유용 할 수 있습니다.
str = '파이썬 2.x 에서는 StringIO가 파이썬 3.x에서는 io.StringIO로 바뀌었습니다.'
f=io.StringIO(str + "\n" + str + "\n" + str + "\n"  + str + "\n" )
print(f.readline()[:-1])
print(f.readline()[:-1])
print()
f.seek(0)
print(f.read(100))
print()
f.seek(0)
print(f.read())
f.close()

