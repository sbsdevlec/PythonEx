import glob
import os
import io
# 텍스트 파일 처리( In-memory Streams )
# 파이썬 2.x 에서는 StringIO가 파이썬 3.x에서는 io.StringIO로 바뀌었습니다.
# StringIO는 파일처럼 흉내내는 객체라고 이해하면 됩니다.
# 문자열 데이터를 파일로 저장한 다음 여러가지 처리를 하게 되는데 그 파일이 다시 쓰이지 않을 때 유용하게 사용된다고 한다.
str = '파이썬 2.x 에서는 StringIO가 파이썬 3.x에서는 io.StringIO로 바뀌었습니다.'
f=io.StringIO()
f.write(str+"\n")
f.write(str+"\n")
f.write(str+"\n")
#f.flush()
# 모든 데이터 읽기
print(f.getvalue())
f.close()

