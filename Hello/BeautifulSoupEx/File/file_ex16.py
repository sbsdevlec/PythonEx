import glob
import os
import io
# 텍스트 파일 처리( In-memory Streams )
# 유니 코드 텍스트 대신 원시 바이트로 작업하려면을 BytesIO 사용하십시오
str = '유니 코드 텍스트 대신 원시 바이트로 작업하려면을 BytesIO 사용하십시오'
f = io.BytesIO()
f.write(str.encode('UTF-8'))
print(f.getvalue())
f.close()

str = '유니 코드 텍스트 대신 원시 바이트로 작업하려면을 BytesIO 사용하십시오'.encode('UTF-8')
# print(str)
f = io.BytesIO(str)
print(f.read())

f.close()
f = io.BytesIO(str)
print(f.read().decode("utf-8"))
f.close()
print()

output = io.BytesIO()
output.write('This goes into the buffer. '.encode('utf-8'))
output.write('한글'.encode('utf-8'))
print(output.getvalue())
output.close()

output = io.BytesIO()
output.write('This goes into the buffer. '.encode('utf-8'))
output.write('한글'.encode('utf-8'))
print(output.getvalue().decode("utf-8"))
output.close()
print()

# Initialize a read buffer
output = io.BytesIO(b'Inital value for read buffer')
print(output.read())
output.close()

output = io.BytesIO(b'Inital value for read buffer')
print(output.read().decode("utf-8"))
output.close()
print()

# Initialize a read buffer
output = io.BytesIO('Inital value for read buffer 한글'.encode('utf-8'))
print(output.read())
output.close()
output = io.BytesIO('Inital value for read buffer 한글'.encode('utf-8'))
print(output.read().decode("utf-8"))
output.close()