from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

print(timedelta(days = 300, hours = 4, minutes = 116))

print("Today is: " + str(datetime.now()))

print("One year from now it will be: " + str(datetime.now() + timedelta(days = 365)))

print("In two weeks, three days, and fourteen hours, it will be: " + str(datetime.now() + timedelta(weeks = 2, days = 3, hours = 14)))

t = datetime.now() - timedelta(weeks = 1)
s  = t.strftime("%A, %B %d, %Y")
print("One week ago it was " + str(s))

print(" ")

today = date.today()
afd = date(today.year, 4, 1)
if afd < today:
    print("April Fools' Day happened %d days ago." %((today-afd).days))
    afd = afd.replace(year=today.year+1)

time_to_afd = abs(afd - today)
print(time_to_afd.days, "days until April Fools' Day next year.")