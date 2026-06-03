# 9.wap to find out wheather a file is identical and matches the content of another file

with open('file.txt') as f:
    content1 = f.read()

with open('log.txt') as f:
    content2 = f.read()

if content1 == content2:
    print("They're both same")
else:
    print("They're different.")