"""
파이썬은 객체지향 프로그래밍(OOP, Object Oriented Programming)을 기본적으로 지원하고 있다. 
파이썬에서 객체지향 프로그래밍의 기본 단위인 클래스를 만들기 위해서는 아래와 같이 "class 클래스명" 을 사용하여 정의한다. 
클래스명은 PEP 8 Coding Convention에 가이드된 대로 각 단어의 첫 문자를 대문자로 하는 CapWords 방식으로 명명한다. 
아래 예제는 Some라는 클래스를 정의한 것으로 별도의 클래스 멤버를 정의하지 않은 가장 간단한 빈 클래스이다. 
클래스 정의 내의 pass문은 빈 동작 혹은 아직 구현되지 않았음을 의미하는 것으로 여기서는 빈 클래스를 의미한다.
"""
class Some:
    """
    아무일도 하지않는 클래스입니다.
    """
    pass

s1 = Some()
print(s1)
print(s1.__doc__)
print(s1.__class__)
print(s1.__class__.__name__)
print(s1.__class__.__bases__)