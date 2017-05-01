import sys
import os

# 바이너리 파일의 사용
# 파일이나 네트워크 연결에 저장된 바이너리 데이터를 처리 하는데 사용

# str <---> bytearray/bytes 변환
# 인코딩(encode) : 유니코드 --> 다른 characterset
# 디코딩(decode) : 다른 characterset --> 유니코드
# decode 메서드가 str(바이트스트링, encoding='utf-8')로 변경됨

print(sys.getdefaultencoding())
string = 'Python 파이선'
print(type(string), string)
binary = string.encode()
print(type(binary), binary)
print(binary.decode('utf-8'))
print(str(binary,encoding='utf-8'))
print()

str1 = 'Python 파이선'
str2 = bytes(str1, encoding='utf-8')
str3 = str1.encode('utf-8')
str4 = str3.decode('utf-8')
print(type(str1), type(str2), type(str3), type(str4))
print(str1, str2, str3, str4)
print( str1 == str2 )
print( str3 == str4 )
print( str1 == str4 )
print( str2 == str3 )
print()