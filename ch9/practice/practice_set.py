#1. write a program to read the text from a given file 'poems.txt' and find out  if it contains word 'twinkle'

f = open('ch9/poems.txt', 'r')
data = f.read()
if 'twinkle' in data:   #this search for each letters in given order. if the file has twinkle but in this line 'twinkle' is replaced by nkle, if it has word nkle even in word 'twinkle' it is true.
    print("This contains twinkle")
else:
    print("This doesn't contain any twinkle word")


