#can open multiple files using single context manager:

with(
    open('file1.txt') as f1,
    open('file1.txt') as f2,
):
    f1.read()
    f2.read()