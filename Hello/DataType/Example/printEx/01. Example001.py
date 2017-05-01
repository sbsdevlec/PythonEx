import math
print('Hello World!!')
print("Hello World!!")
print("Hello \tWorld!!")
print("Hello \nWorld!!")
print("나의 이름은 '한사람'입니다.")
print("나의 이름은 \"한사람\"입니다.")
print('나의 이름은 "한사람"입니다.')
print('나의 이름은 \'한사람\'입니다.')
print('-' * 40)

print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'.format( food='spam', adjective='absolutely horrible'))
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
print('-' * 40)

contents = 'eels'
print('My hovercraft is full of {}.'.format(contents))
print('My hovercraft is full of {!r}.'.format(contents))
print('The value of PI is approximately {0:.3f}.'.format(math.pi))
print('The value of PI is approximately {0:.7f}.'.format(math.pi))
print('-' * 40)

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))

print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
print('-' * 40)

for x in range(1, 6):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print('-' * 40)
# Old string formatting
print('The value of PI is approximately %5.3f.' % math.pi)
print('-' * 40)

