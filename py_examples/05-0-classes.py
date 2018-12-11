
class myClass():
    def method1(self):
        print("myClass method1")
    
    def method2(self, someString):
        print("myclass method2: " + someString)
    
class anotherClass(myClass):
    def method2(self):
        print("anotherClass method2")
    def method1(self):
        #do this to add something to myClass method1 
        myClass.method1
        print("anotherClass method1")

def main():
    c = myClass()
    c.method1()
    c.method2("some string")
    c2 = anotherClass()
    c2.method1()
    c2.method2()

main()