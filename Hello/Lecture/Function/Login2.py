# 예외 클래스 작성
class LoginError(Exception):
    """3회 이상 틀렸으므로 다시 인증을 받아야 합니다."""
    pass

# count변수를 전역변수로 뺐습니다.
count = 0
# count = 3 # 초기값을 3으로 준다면 어떻게 될까요?

def login(userid,password):
    global count # 전역 변수의 사용을 알렸습니다.
    # 여기서는 id가 admin이고 password가 root이면 로그인처리를 하자
    if userid=='admin' and password=='root':
        return True
    else:
        count += 1
        print("{}번 실패".format(count))
        # 3회이상 틀리면 예외발생
        if count==3: raise LoginError() 
        return False
# 메인
try:
    while True:
        id = input('아이디를 입력하시오')
        password = input('암호를 입력하시오')
        if login(id,password): break
        count += 1 # 여기에서 count값을 변경한다면 어떻게 될까요?
except LoginError:
    print(LoginError.__doc__)
else:
    print(id+"님 환영합니다.")