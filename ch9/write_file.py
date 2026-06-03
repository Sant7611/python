st = "This is the updated string"
f = open("ch9/myfile.txt", "w") #create new file if not found then opens it

f.write(st)
f.close()