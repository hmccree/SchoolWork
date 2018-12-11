import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    print(os.name)
    print("Item exists: " + str(path.exists("10-1-testfile.txt")))
    print("Item is a file: " + str(path.isfile("10-1-testfile.txt")))
    print("Item is a directory: " + str(path.isdir("10-1-testfile.txt")))
    print("Item's path: " + str(path.realpath("10-1-testfile.txt")))
    print("Item's path and name: " + str(path.split(path.realpath("10-1-testfile.txt"))))

    t = time.ctime(path.getmtime("10-1-testfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("10-1-testfile.txt")))

    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("10-1-testfile.txt"))
    print("It has been " + str(td) + " since the file was modified")
    print("Or, " + str(td.total_seconds()) + " seconds")


main()