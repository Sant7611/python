l = [2,3,4,5,6,7,8,9]

index = 0
for item in l:
    print(f"The item number {index} is {item}")
    index +=1

#instead we can do this.

for index, item in enumerate(l):
    print(f"The item number {index} is {item}")
    