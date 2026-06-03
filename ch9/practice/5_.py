#5.repeat program 4 for a list of such words to be censored.

word = ['Donkey', 'bad','don']

with open('4file.txt', 'r') as f:
    content = f.read()
for i in word:
    content = content.replace(i, '#' * len(i))

print(content)

with open('file.txt', 'w') as f:
    f.write(content)