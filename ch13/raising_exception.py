a = int(input("Enter any number: "))
b = int(input("Enter second number: "))

class ZeroException(Exception):
    pass

if(b==0):
    raise ZeroException("You are divding by szero")
else:
    print(a/b)