import datetime

print('Now    :', datetime.datetime.now())
print('Today  :', datetime.datetime.today())
print('UTC Now:', datetime.datetime.utcnow())
print("-"*30)

now = datetime.datetime.now()
print(now)
print('ctime:', now.ctime())
print('tuple:', now.timetuple())
print('ordinal:', now.toordinal())
print('Year:', now.year)
print('Mon :', now.month)
print('Day :', now.day)
print('Hour :', now.hour)
print('Minute :', now.minute)
print('Second :', now.second)
print("-"*30)

today = datetime.datetime.today()
print(today)
print('ctime:', today.ctime())
print('tuple:', today.timetuple())
print('ordinal:', today.toordinal())
print('Year:', today.year)
print('Mon :', today.month)
print('Day :', today.day)
print('Hour :', today.hour)
print('Minute :', today.minute)
print('Second :', today.second)
print("-"*30)

utc = datetime.datetime.utcnow()
print(today)
print('ctime:', utc.ctime())
print('tuple:', utc.timetuple())
print('ordinal:', utc.toordinal())
print('Year:', utc.year)
print('Mon :', utc.month)
print('Day :', utc.day)
print('Hour :', utc.hour)
print('Minute :', utc.minute)
print('Second :', utc.second)
print("-"*30)

d = datetime.datetime.now()
for attr in [ 'year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
    print(attr, ':', getattr(d, attr))
print("-"*30)

print("Current date and time: " , datetime.datetime.now())
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))
print("-"*30)

t = datetime.time(1, 2, 3)
print('t :', t)
d = datetime.date.today()
print('d :', d)
dt = datetime.datetime.combine(d, t)
print('dt:', dt)
print("-"*30)

format = "%a %b %d %H:%M:%S %Y"
today = datetime.datetime.today()
print('ISO     :', today)
s = today.strftime(format)
print('strftime:', s)
d = datetime.datetime.strptime(s, format)
print('strptime:', d.strftime(format))
print("-"*30)

'''
Note: Examples are based on datetime.datetime(2013, 9, 30, 7, 6, 5)
Code	Meaning	Example
%a	Weekday as locale’s abbreviated name.	Mon
%A	Weekday as locale’s full name.	Monday
%w	Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.	1
%d	Day of the month as a zero-padded decimal number.	30
%-d	Day of the month as a decimal number. (Platform specific)	30
%b	Month as locale’s abbreviated name.	Sep
%B	Month as locale’s full name.	September
%m	Month as a zero-padded decimal number.	09
%-m	Month as a decimal number. (Platform specific)	9
%y	Year without century as a zero-padded decimal number.	13
%Y	Year with century as a decimal number.	2013
%H	Hour (24-hour clock) as a zero-padded decimal number.	07
%-H	Hour (24-hour clock) as a decimal number. (Platform specific)	7
%I	Hour (12-hour clock) as a zero-padded decimal number.	07
%-I	Hour (12-hour clock) as a decimal number. (Platform specific)	7
%p	Locale’s equivalent of either AM or PM.	AM
%M	Minute as a zero-padded decimal number.	06
%-M	Minute as a decimal number. (Platform specific)	6
%S	Second as a zero-padded decimal number.	05
%-S	Second as a decimal number. (Platform specific)	5
%f	Microsecond as a decimal number, zero-padded on the left.	000000
%z	UTC offset in the form +HHMM or -HHMM (empty string if the the object is naive).
%Z	Time zone name (empty string if the object is naive).
%j	Day of the year as a zero-padded decimal number.	273
%-j	Day of the year as a decimal number. (Platform specific)	273
%U	Week number of the year (Sunday as the first day of the week) as a zero padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.	39
%W	Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0.	39
%c	Locale’s appropriate date and time representation.	Mon Sep 30 07:06:05 2013
%x	Locale’s appropriate date representation.	09/30/13
%X	Locale’s appropriate time representation.	07:06:05
%%	A literal '%' character.	%
'''