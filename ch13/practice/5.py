from ques3 import table

items = table()
with open('ch13/practice/table.txt', 'a+') as f:
    for i in items:
        f.write(f"{str(i)} ")
    f.write('\n')
    f.seek(0)
    content = f.read()

print(content)