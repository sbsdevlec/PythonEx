import glob
import os
import io
# 텍스트 데이터 용 바이트 스트림 래핑
# 소켓과 같은 원시 바이트 스트림은 문자열 인코딩 및 디코딩을 처리하는 레이어로 래핑 할 수 있으므로 텍스트 데이터와 함께 쉽게 사용할 수 있습니다.
# 이 TextIOWrapper는 읽기뿐만 아니라 쓰기도 지원합니다.
# write_through인수 버퍼링을 비활성화하고 바로 기본 버퍼 통해 랩퍼에 기록 된 모든 데이터를 플러시한다.

# Writing to a buffer
output = io.BytesIO()
wrapper = io.TextIOWrapper(
    output,
    encoding='utf-8',
    write_through=True,
)
wrapper.write('This goes into the buffer. ')
wrapper.write('한글은 어떻게?')
s  = output.getvalue()
print(s)
print(s.decode('UTF-8'))
output.close()
print()


# Initialize a read buffer
input = io.BytesIO(
    b'Inital value for read buffer with unicode characters ' +
    '한글은 어떻게?'.encode('utf-8')
)
wrapper = io.TextIOWrapper(input, encoding='utf-8')

# Read from the buffer
print(wrapper.read())