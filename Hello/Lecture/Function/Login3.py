# 예외 클래스 작성
class LoginError(Exception):
    """3회 이상 틀렸으므로 다시 인증을 받아야 합니다."""
    pass

def login(userid,password):
    # 여기서는 id가 admin이고 password가 root이면 로그인처리를 하자
    if userid=='admin' and password=='root':
        return True
    else:
        login.count += 1
        print("{}번 실패".format(login.count))
        # 3회이상 틀리면 예외발생
        if login.count==3:
            raise LoginError()
        return False

login.count = 0 # 클래스 내에 속성을 하나 만듭니다.
#login.count = 3

# 메인
try:
    while True:
        id = input('아이디를 입력하시오')
        password = input('암호를 입력하시오')
        if login(id,password): break
        #login.count += 1
except LoginError:
    print(LoginError.__doc__)
else:
    print(id+"님 환영합니다.")