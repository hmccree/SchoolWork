
def main():
    x = 0
    while (x < 5):
        print("x equals " + str(x))
        x += 1
    for y in range(5, 10):
        print("y equals " + str(y))
    days = ["Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun"]
    for d in days:
        print(d)

# for x in range(1,24):
#     #if(x == 9): break
#     if(x%2 == 0): continue
#     print(x)

days = ["Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun"]
for i, d in enumerate(days):
    print(i, d)




#main()