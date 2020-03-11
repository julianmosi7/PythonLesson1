x, y, z = 5, "Hello, World!", " Awesome"
a = y + z
#printing Hello, World!
print(y)
if x > 2:
    print("Five is greater than two!")
    print(y + " My name is Julian")
    print(a)


#global and local variables
b = "awesome"
def myfunc():
    #global b
    b = "fantastic"
    print("Python is " + b)

myfunc()

print("Python is " + b)


