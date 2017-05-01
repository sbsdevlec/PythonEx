import calendar

calendar.prcal(2017)
calendar.prmonth(2017,3)

calendar.TextCalendar(calendar.SUNDAY).prmonth(2017,3)
c = calendar.TextCalendar(calendar.SUNDAY)
c.prmonth(2017, 3)

c = calendar.HTMLCalendar(calendar.SUNDAY)
print(c.formatmonth(2017, 3))

