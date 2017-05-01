def hi1(): print('안녕하세요')

def hi2():
    print('안녕하세요')

#def hi3():
#print('안녕하세요')
'''
들여쓰기를 하지 않으면 다음과 같은 에러 발생
  File "C:/Users/DJA/PycharmProjects/Lecture/Function/fn01.py", line 7
    print('안녕하세요')
        ^
  IndentationError: expected an indented block
'''

def hi3():
    print('안녕하세요')
print('이 줄은 어디에 속한걸까요?')

hi1()
hi2()
hi3()