from functools import singledispatch

@singledispatch
def function(arg):
    print('문자열', arg, type(arg))

@function.register(int)
def _(arg):
    print('정수', arg, type(arg))

@function.register(float)
def _(arg):
    print('실수', arg, type(arg))

@function.register(type(None))
def _(arg):
    print('인수가 없습니다.')

function(None)
function("안녕 Python")
function(123)
function(3.14)
