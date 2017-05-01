a=1
b=1
print(a is b, id(a), id(b))
print()

a=1.0
b=1.0
print(a is b, id(a), id(b))
print()

a='str'
b='str'
print(a is b, id(a), id(b))
print()

a=(1,2,3)
b=(1,2,3)
print(a is b, id(a), id(b))
print()

a=[1,2,3]
b=[1,2,3]
print(a is b, id(a), id(b))
print()

a={'name':'kimc'}
b={'name':'kimc'}
print(a is b, id(a), id(b))
print()


