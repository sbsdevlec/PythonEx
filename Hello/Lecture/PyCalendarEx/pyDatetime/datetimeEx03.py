import datetime
import time

today = datetime.date.today()
print(today)
print('ctime:', today.ctime())
print('tuple:', today.timetuple())
print('ordinal:', today.toordinal())
print('Year:', today.year)
print('Mon :', today.month)
print('Day :', today.day)
print("-"*30)

print('Earliest  :', datetime.date.min)
print('Latest    :', datetime.date.max)
print('Resolution:', datetime.date.resolution)
print("-"*30)

d1 = datetime.date(2017, 3, 12)
print('d1:', d1)
d2 = d1.replace(year=2018)
print('d2:', d2)
d3 = d2.replace(month=5,day=5)
print('d3:', d3)
print("-"*30)

print("microseconds:", datetime.timedelta(microseconds=1))
print("milliseconds:", datetime.timedelta(milliseconds=1))
print("seconds     :", datetime.timedelta(seconds=1))
print("minutes     :", datetime.timedelta(minutes=1))
print("hours       :", datetime.timedelta(hours=1))
print("days        :", datetime.timedelta(days=1))
print("weeks       :", datetime.timedelta(weeks=1))
print("-"*30)

today = datetime.date.today()
print('Today    :', today)

one_day = datetime.timedelta(days=1)
print('One day  :', one_day)

yesterday = today - one_day
print('Yesterday:', yesterday)

tomorrow = today + one_day
print('Tomorrow :', tomorrow)

print('tomorrow - yesterday:', tomorrow - yesterday)
print('yesterday - tomorrow:', yesterday - tomorrow)
print("-"*30)

