d = {} # {} <class 'dict'>
print(d, type(d))
nums = [1, 2, 3]
# d[nums] = "hello"

d[tuple(nums)] = "hello" # {(1, 2, 3): 'hello'} <class 'dict'>
print(d, type(d))

addr = 'monty@python.org'
uname, domain = addr.split('@')
print(uname)
print(domain)

# 튜플 반환 값
t = divmod(7, 3)
print(t)

quot, rem = divmod(7, 3)
print(quot)
print(rem)

# 가변길이 인자 튜플
def printall(*args):
    print(args)

printall(1, 2.0, '3')

t = (7, 3)
# print(divmod(t))
# TypeError: divmod expected 2 arguments, got 1
print(divmod(*t)) # (2, 1)
