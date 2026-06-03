
#3.wap to generate mutiplication tables from 2 to 20 and write it to the different file. place these files in a folder for a 13-yrs old.
for i in range(2,21):
    table = ""
    for j in range(1,11):
        table += f"{i} x {j} = {i*j} \n"

    with open('ch9/practice/3file.txt', 'a') as f:
        f.write(table)
