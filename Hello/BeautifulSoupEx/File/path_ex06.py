import os

path1 = r"c:\windows\system32"
path2 = r"c:\windows\system32\write.exe"

# 현재 경로를 Prefix로 하여 입력받은 경로를 절대경로로 바꿔서 반환합니다.
print(os.path.abspath('.'))
print(os.path.abspath('temp'))
print()

# 입력받은 경로의 기본 이름(base name)을 반환합니다.
# abspath() 함수와 반대되는 기능을 수행한다고 볼 수 있습니다.
print(os.path.basename(path1))
print(os.path.basename(path2))
print()

# 입력받은 파일/디렉터리의 경로를 반환합니다.
print(os.path.dirname(path1))
print(os.path.dirname(path2))
print()

# 디렉토리인지 확인
print(os.path.isdir(path1))
print(os.path.isdir(path2))
print()

# 파일인지 확인
print(os.path.isfile(path1))
print(os.path.isfile(path2))
print()

# 존재하는지 확인
print(os.path.exists(path1))
print(os.path.exists(path2))
print()

# 입력받은 경로에 대한 바이트 단위의 파일크기를 반환.
# (파일이 없거나 권한이 없는 경우 os.error 예외 발생)
print(os.path.getsize(path1))
print(os.path.getsize(path2))
print()

# os.path.normcase(path)
# 해당 OS에 맞도록 입력 받은 경로의 문자열을 정규화 합니다.
# (윈도우와 같은 경우, 아래 예제와 같이 소문자로 바꾸고 '/'를 '\\'로 변경합니다)
# os.path.normpath(path)
# 입력 받은 경로를 정규화합니다. (현재 디렉터리(".")나 상위 디렉터리("..")와 같은 구분자를 최대한 삭제)
mixed = "c:\\temp\\test/files/test.txt"
print(os.path.normpath(mixed))
print(os.path.normcase(mixed))
print()

# 유니크한 프로세스 ID를 보여준다.
print(os.getpid())
print()

# 입력받은 path_list로부터 공통적인 Prefix를 추출해서 반환합니다. 그러나 이 결과는 문자열 연산에
# 의한 것이기 때문에 다음의 두 번째 예제와 같이 잘못된 경로가 나올 수도 있습니다.
print(os.path.commonprefix(['C:\\Python30\\Lib', 'C:\\Python30', 'C:\\Python30\\Tools']))
print(os.path.commonprefix(['C:\\Python26\\Lib', 'C:\\Python25\\Tools']))
print()

# 입력받은 경로안의 "~"를 현재 사용자 디렉터리의 절대경로로 대체합니다.
# "~"에 붙여서 <사용자명>을 붙이면 원하는 사용자 경로로 대체됩니다.
# (유닉스/리눅스의 홈디렉터리를 나타내는 '~'과 동일합니다)
print(os.path. expanduser('~\\project'))
print()

# path안에 환경변수가 있다면 확장합니다. (환경변수는 os.environ에 정의된 것을 참조)
print(os.path.expandvars('$JAVA_HOME\\bin'))
print(os.path.expandvars('$SYSTEMROOT\\temp'))
print()

# 입력받은 경로에 대한 최근 접근 시간을 반환 (반환되는 값은 epoch(1970년 1월 1일) 이후
# 초단위로 반환됩니다. 파일이 없거나 권한이 없는 경우 os.error 예외 발생)
print(os.path.getatime(path1))
print(os.path.getatime(path2))
# 읽을 수 있는 형식으로 보려면 다음과 같이 하면 됩니다.
import time
print(time.gmtime(os.path.getatime(path1)))
print(time.gmtime(os.path.getatime(path2)))
print()

# 입력받은 경로에 대한 최근 변경 시간을 반환 (파일이 없거나 권한이 없는 경우 os.error 예외 발생)
print(time.gmtime(os.path.getmtime(path1)))
print(time.gmtime(os.path.getmtime(path2)))
print()

# 입력받은 경로에 대한 생성시간을 반환 (유닉스와 같은 운영체제에서는 생성시간이 아닌
# 최근 변경 시간을 반환할 수도 있습니다. 파일이 없거나 권한이 없는 경우 os.error 예외 발생)
print(time.gmtime(os.path.getctime(path1)))
print(time.gmtime(os.path.getctime(path2)))
print()

# 경로가 절대경로이면 True를 반환하고, 그 외의 경우에는 False를 반환.
# (실제 해당 경로를 검사하지는 않으며 입력받은 문자열을 가지고 판단합니다.)
print(os.path.isabs(path1))
print(os.path.isabs('./test/file.txt'))


