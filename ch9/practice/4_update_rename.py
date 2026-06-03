word = 'Donkey'

with open('4file.txt', 'r') as f:
    content = f.read()
newContent = content.replace('Donkey', '######')

with open('file.txt', 'w+') as f:
    f.write(newContent)
    f.seek(0)
    res = (f.read())
    print(res)