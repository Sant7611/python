def greet(name): #function defination
    print("Hello, " + name + ". Good morning!")


greet("Ram")        #function calling

def wish(name):
    print(f"hello {name} we wish you good luck")
    return name     #return value

ret = wish("Santosh")
print(ret)

