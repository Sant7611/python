# without walrus

val = input("Enter the name: ")
if val != "":
    print(val)


#using walrus:
if(val := input("Enter the name: ") ) != "":
    print(val)

