# def recursion(n):
#     if(n <= 0):
#         return 1
#     return (n* recursion(n-1))


# n = int(input("Enter the number  to find factorial: "))
# recur = recursion(n)
# print(recur)

#func to print sum of first n natural numbers:
n = int(input("Enter the number to find the sum: "))
def natural(n):
    # total = n
    if n <= 0:
        return 0
    return n + natural(n-1)

print(natural(n))