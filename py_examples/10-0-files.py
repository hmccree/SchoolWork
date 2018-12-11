
def main():
    #f = open("10-1-testfile.txt", "w+")
    # f = open("10-1-testfile.txt", "w+")

    # for i in range(10):
    #     f.write("This is line %d\r\n" % (i+1))

    # f.close()

    f = open("10-1-testfile.txt", "r")
    if f.mode == "r":
        fl = f.readlines()
        for x in fl:
            print(x)


main()