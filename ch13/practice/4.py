#wap to display a/b where a and b are int. if b = 0, display infinite by handling the 'ZeroDivisionError'

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

try:
    num3 = num1/num2

except ZeroDivisionError as e:
   print('infinite')
