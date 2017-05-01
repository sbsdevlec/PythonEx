import datetime
import time
today = datetime.date.today()
to = today.toordinal()
print('to:', to)
print('fromordinal(to):', datetime.date.fromordinal(to))
o = to + 100
print('o:', o)
print('fromordinal(o):', datetime.date.fromordinal(o))

t = time.time()
print('t:', t)
print('fromtimestamp(t):', datetime.date.fromtimestamp(t))
print('fromtimestamp(t):', datetime.date.fromtimestamp(t+100000))

print("-"*30)

