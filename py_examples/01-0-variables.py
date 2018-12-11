f=0
print (f)

f="abc"
print (f)

#print ("string type " + str(123))

def function():
    global f
    f="def"
    print(f)

function()
print(f)

del f
print(f)