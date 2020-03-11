x = 5
print(type(x))

b = "Hello, World!"
print(b[2:4])
print(b.upper())
x = "el" in b
y = "ol" in b
print(x)
print(y)

age = 18
txt = "My name is Julian, and I am {0} years old"
print(txt.format(age))

a = "Python is the most awesome programming language"
partOne = a[a.find("the"):50]
partOne = partOne.replace(partOne[0:1], partOne[0:1].upper())
partTwo = a[a.find("is"):a.find("the")-1]
partThree = a[a.find("Python"):a.find("is")-1]
result = "{} {} {}, even in 2020."
print(result.format(partOne, partTwo, partThree))

