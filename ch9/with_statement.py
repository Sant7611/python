# f.close()  

f = open('ch9/file.txt')
print(f.read())
f.close()

#the same as abve can be written as:
with open("ch9/file.txt") as f:
    print(f.read())

#using this statement, you don't have to explicitly close the file

