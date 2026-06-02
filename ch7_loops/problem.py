# num = int(input("Enter any number: "))

# for i in range(1, 11):
#     print(f" {num} x {i} = {num * i} ")

# # 2.
# num = int(input("Enter any number: "))
# prime = True
# for i in range(2, num):
#     if num % i == 0:
#         prime = False
#         break

# if prime:
#     print("The number is prime.")
# else:
#     print("The number is not primme")


#3.

# n = int(input("Enter the number: "))
# for i in range(1, n+1):
#     print(" " * (n-i), end="" )
#     print("*" * (2*i-1), end="")
#     print("")


#4.
# n = int(input("Enter the number: "))
# for i in range(1, n+1):
    # print(" " * (n - i), end="")
#     print("*"* (i), end="")
#     print("")

# #5.
# n = int(input("Enter the number: "))
# for i in range(1,n +1):
#     if(i == 1 or i == n):
#         print("*" * n, end="")
#     else:
#         print("*", end="")
#         print(" " * (n-2), end="")
#         print("*", end="")
#     print("")


#6.
n = int(input("Enter the number: "))
for i in range(10, 0, -1):
    print(f"{n} x {i} = {n* i}")
    
