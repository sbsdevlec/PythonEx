# 문자열 표시
print("qwerty12345문자열")
print('qwerty12345문자열')
print("""qwerty12345문자열""")
print('''qwerty12345문자열''')

#문자열내에 특수문자 표현
str = '당신의 이름은 "한사람"입니다.'
print(str)
str = "당신의 이름은 '한사람'입니다."
print(str)
str = '당신의 이름은 \'한사람\'입니다.'
print(str)
str = "당신의 이름은 \"한사람\"입니다."
print(str)

# 긴 문자열의 표현
longstr = '''
아주 아주 긴 문자열이라고 생각하자.
아주 아주 긴 문자열이라고 생각하자.
아주 아주 긴 문자열이라고 생각하자.
'''
print(longstr)
longstr = """
아주 아주 긴 문자열이라고 생각하자.
아주 아주 긴 문자열이라고 생각하자.
아주 아주 긴 문자열이라고 생각하자.
"""
print(longstr)
longstr = '''
        아주 아주 긴 문자열이라고 생각하자.
        아주 아주 긴 문자열이라고 생각하자.
        아주 아주 긴 문자열이라고 생각하자.
        '''
print(longstr)
longstr = """
        아주 아주 긴 문자열이라고 생각하자.
        아주 아주 긴 문자열이라고 생각하자.
        아주 아주 긴 문자열이라고 생각하자.
        """
print(longstr)

# 이스케이프 시퀀스는 문자열 내부에 특수한 문자를 정의하는데 사용합니다.
print("하나\t둘\t셋\t\t넷")
print("하나\n둘\n셋\n\n넷")

"""
Escape	What it does.
\\	Backslash (\)
\'	Single-quote (')
\"	Double-quote (")
\a	ASCII bell (BEL)
\b	ASCII backspace (BS)
\f	ASCII formfeed (FF)
\n	ASCII linefeed (LF)
\N{name}	Character named name in the Unicode database (Unicode only)
\r	Carriage Return (CR)
\t	Horizontal Tab (TAB)
\uxxxx	Character with 16-bit hex value xxxx (u'' string only)
\Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx (u'' string only)
\v	ASCII vertical tab (VT)
\ooo	Character with octal value ooo
\xhh	Character with hex value hh
"""


