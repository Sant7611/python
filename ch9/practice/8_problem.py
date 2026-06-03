
# 8.wap to make a copy of a txt file 'this.txt'
with open('log.txt') as f:
    content = f.read()

with open('file.txt', 'w') as f:
    f.write(content)