#wap for list comprehension to print a list which contains the multiplication table of a user entered number.

def table():
    userInput = int(input("Enter the number to find the table: "))
    table = [userInput* i for i in range(1,11)]
    print(table)
    return table

if __name__ == '__main__':
    table()
    print('This ran in the file where the code is written.')