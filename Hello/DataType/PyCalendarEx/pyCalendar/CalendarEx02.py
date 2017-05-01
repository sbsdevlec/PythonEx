import calendar
# set firstweekday=0
cal= calendar.Calendar(firstweekday=0)
for x in cal.iterweekdays():
    print(x, end=" ")
print()

print("-"*50)

# set firstweekday=1
cal= calendar.Calendar(firstweekday=1)
for x in cal.iterweekdays():
    print(x, end=" ")
print()

print("-" * 50)

cal= calendar.Calendar()
for x in cal.itermonthdates(2017, 3):
    print(x)
print()

print("-" * 50)

cal= calendar.Calendar()
for x in cal.itermonthdays2(2017, 3):
    print(x)
print()

print("-" * 50)