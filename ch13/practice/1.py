#wap to open three files 1.txt, 2, 3 . if any of these files are not present, a msg without exitingthe program must be printed prompting the same. 

try:

    with(
        open('file1.txt') as f1,
        open('file2.txt') as f2,
        open('file3.txt') as f3
    ):
        f1.read()
        f2.read()
        f2.read()
except Exception as e:
    print(e)

finally:
    print("This uses try catch and opening multple files.")