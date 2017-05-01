# -------------------------------------------------------------------
# https://pyformat.info/ 참조하세요
# -------------------------------------------------------------------

person = {"name":"한사람","age":33}
print(person)
print("{name}씨 {age}살이네".format(**person))
print("{p[name]}씨 {p[age]}살이네".format(p=person))
print()
data = [4, 8, 15, 16, 23, 42]
print("{d[3]} {d[1]}".format(d=data))
print()

#객체
class Plant(object):
    type = 'tree'

print("{p.type}".format(p=Plant()))

class Plant2(object):
    type = 'tree'
    kinds = [{'name': 'oak'}, {'name': 'maple'}]

print('{p.type}: {p.kinds[1][name]}'.format(p=Plant2()))

#날짜
from datetime import datetime
print('{:%Y-%m-%d %H:%M}'.format(datetime(2017, 2, 3, 4, 5)))

#사용자지정
print("'{:{align}{width}}'".format('test', align='^', width='10'))
print('{:.{prec}} = {:.{prec}f}'.format('실수형자료', 2.7182, prec=3))
print('{:{width}.{prec}f}'.format(2.7182, width=5, prec=2))
print('{:{prec}} = {:{prec}}'.format('실수형자료', 2.7182, prec='.3'))
dt = datetime(1,2,3,4,5,6)
print('{:{dfmt} {tfmt}}'.format(dt, dfmt='%Y-%m-%d', tfmt='%H:%M'))
print("'{:{}{}{}.{}}'".format(2.7182818284, '>', '+', 10, 3))
print("'{:{}{sign}{}.{}}'".format(2.7182818284, '>', 10, 3, sign='+'))

class HAL9000(object):
    def __format__(self, format):
        if (format == 'open-the-pod-bay-doors'):
            return "I'm afraid I can't do that."
        return 'HAL 9000'

print('{}'.format(HAL9000()))
print('{:open-the-pod-bay-doors}'.format(HAL9000()))

