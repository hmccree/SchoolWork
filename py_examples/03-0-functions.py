def func1():
    print("I am function 1")

# func()
# print(func())
# print(func)


def func2(arg1, arg2):
    print(arg1, " ", arg2)


def cube(x):
    return x*x*x

#func2(10, 20)
# print(func2(10,20))
# print(cube(6))


def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

#print(power(2))
#print(power(4,3))
#print(power(x=3, num=3))

def multi_add(*args):
    result = 0
    for x in args:
        result += x
    return result

#print(multi_add(4,6,11,89,4,3,90,54,2,0,76,22))