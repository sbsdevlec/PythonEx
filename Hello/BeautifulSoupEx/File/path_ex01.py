import os
# os.path는 파일 경로를 생성 및 수정하고, 파일 정보를 쉽게 다룰 수 있게 해주는 모듈.
# os의 이름, 경로, 환경변수 알아보기
print(os.name)
print()
print(os.environ['PATH'])
print()
env = os.environ
print(type(env))
print(vars(env))
for key in env:
    print(key, ":", env[key])