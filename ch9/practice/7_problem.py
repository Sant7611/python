# 7. wap to find out the line number where python is present from q.6


with open('log.txt') as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if 'python' in line:
        print("The word is present in line", lineno)
        break
    lineno+=1
else:
    print("The word is not present")