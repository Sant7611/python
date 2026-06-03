#6.wap to mine a log file and find out wheater it contains 'python'
word = 'python'
with open('log.txt', 'r') as f:
    content = f.read()
if word in content:
    print("This file contains python word")
else:
    print("This file doesn't contain python word")