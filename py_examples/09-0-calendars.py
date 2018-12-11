import calendar

#ASCII calendar
c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2018,11,0,0)
print(str)

#HTML calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
str = hc.formatmonth(2018,11)
# print(str)

#iterate through days of calendar
for i in c.itermonthdays(2018,11):
    print(i)

print("-----------------------------")

for name in calendar.month_name:
    print(name)

print("-----------------------------")

for day in calendar.day_name:
    print(day)

print("-----------------------------")

#Print the first friday of each month
for m in range(1,13):
    cal = calendar.monthcalendar(2018,m)
    weekone = cal[0]
    weektwo = cal[1]
    if(weekone[calendar.FRIDAY] != 0):
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]
    print("%10s %2d" % (calendar.month_name[m], meetday))

print("-----------------------------")

#print calendars for each month
for m in range(1,13):
    c = calendar.TextCalendar(calendar.SUNDAY)
    str = c.formatmonth(2018,m,0,0)
    print(str)

print("-----------------------------")


#everything else is printing out the months that start on a saturday
# for m in range(1,13):
#     c = calendar.TextCalendar(calendar.SUNDAY)
#     str = c.formatmonth(2018,m,0,0)
#     if(str[59] == "1"):
#         print("%10s %2d" % (calendar.month_name[m], meetday))

for m in range(1,13):
    cal = calendar.monthcalendar(2018,m)
    weekone = cal[0]
    weektwo = cal[1]
    if(weekone[calendar.SATURDAY] != 0):
        meetday = weekone[calendar.SATURDAY]
        if(meetday == 1):
            print("%10s" % (calendar.month_name[m]))
#    else:
#        meetday = weektwo[calendar.SATURDAY]
#    print("%10s %2d" % (calendar.month_name[m], meetday))