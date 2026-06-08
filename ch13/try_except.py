try:
    a = int(input("Enter the number: "))
    print(a)

except Exception as e:
    print(e)

else:
    print("This is after everything ran successfully. by everything i mean try block runs totally and no exception is caught.")

print("Hello this is after error shows up. ")

