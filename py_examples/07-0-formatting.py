from datetime import datetime

def main():
    now = datetime.now()
    #%y and %Y are year, %A and %a are weekday, %B is month, %d is day, etc (not exhaustive list) 
    print(now.strftime("%Y"))
    print(now.strftime("%y"))
    #not US format
    print(now.strftime("%a, %d %B, %y"))
    #locale-based
    print(now.strftime("%c"))

    print(now.strftime("%I:%M:%S %p"))
    print(now.strftime("%H:%M:%S"))

main()