#find the next wednesday, then find ten days from that
import calendar

c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2018,11,0,0)
print(str)

# cal = calendar.monthcalendar(2018,12)
# weekone = cal[0]
# weektwo = cal[1]
# if(weekone[calendar.WEDNESDAY] != 0):
#     meetday = weekone[calendar.WEDNESDAY]
#     meetday += 16
# else:
#     meetday = weektwo[calendar.WEDNESDAY]
#     meetday += 16
# print("%10s %2d" % (calendar.month_name[12], meetday))

