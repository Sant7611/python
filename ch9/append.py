string = 'This is newly added line. using append mode'

f = open('ch9/myfile.txt', 'a')

f.write(string)
f.close()

