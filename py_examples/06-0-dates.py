from datetime import date
from datetime import time
from datetime import datetime

def main():
    today = date.today()
    print("Today's date is ", today)
    print("Date components: ", today.day, today.month, today.year)
    #weekday is a number, 0 is Monday, 6 is Sunday
    #weekday requires extra parens
    print("Today's weekday: ", today.weekday())

    today = datetime.now()
    print("The current date and time is", today)
    
    t = datetime.time(datetime.now())
    print("The current time is ", t)

    

main()