lst = [1,2,3,4,5,6,7,8,9,0]

for index, value in enumerate(lst):
    if index ==2 or index == 4 or index ==6:
        print(f'{index} => {value}')