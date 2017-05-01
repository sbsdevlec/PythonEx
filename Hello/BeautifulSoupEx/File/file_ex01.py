# 파일도 1개의 objectㄹ 구현되어 있어 파일 처리 할 때
# 메서드를 이용하여 처리할 수 있도록 구성되어 있다
# 파일은 라인이라는 요소들로 구성된 하나의 객체이므로 iterable 처리가 가능합니다.

# 실제 파일을 전달하는 것이 아니라 file handle을 전달해서 파일처리함
import glob
import os
# 파일 열기
# 파일객체 = open(파일이름,파일모드)
f = open('newfile.txt','w')
# 파일닫기
# 파일객체.close()
f.close()

files = glob.glob("*.txt")
print(files)
file_path = os.path.abspath('./newfile.txt')
print(file_path)
print(os.path.isfile(file_path))
print(os.path.getsize(file_path))
print()
file_path = './newfile.txt'
print(file_path)
print(os.path.isfile(file_path))
print(os.path.getsize(file_path))

'''
 파일 처리 모드
  - 'r' : 읽기 전용
  - 'w' : 쓰기 전용
  - 'a' : 파일 끝에 추가(쓰기 전용)
  - 'r+' : 읽고 쓰기
  - 'w+' : 읽고 쓰기(기존 파일 삭제)
  - 'a+' : 파일 끝에 추가(읽기도 가능)
  - 'rb' : 이진 파일 읽기 전용
  - 'wb' : 이진 파일 쓰기 전용
  - 'ab' : 이진 파일 끝에 추가(쓰기 전용)
  - 'rb+' : 이진 파일 읽고 쓰기
  - 'wb+' : 이진 파일 읽고 쓰기(기존 파일 삭제)
  - 'ab+' : 이진 파일 끝에 추가(읽기도 가능)
※ 플랫폼에 의존하지 않는 코드를 작성하려 한다면 이진 파일을 다룰 때 b 플래그를 사용하는 것이 좋다.
'''