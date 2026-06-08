a = 75
def fun():
    global a #this changes the global variable.
    a = 3
    print(a)
fun()
print(a) #this refers to the a inside the fun now.
