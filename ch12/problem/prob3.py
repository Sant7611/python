
# class Employee:
#     salary = 19999
#     increment = 20
    
#     @property
#     def salaryAfterIncrement(self):
#         return self.salary + self.salary * (self.increment/100)

#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self, value):
#         # self.salary = value / (1 + self.increment / 100)
#         self.increment = ((value/self.salary) -1 ) * 100
# emp = Employee()

# emp.salaryAfterIncrement = 10000
# print(emp.salaryAfterIncrement)



class Employee:
    def __init__(self, salary=20000, increment=20):
        self.salary = salary
        self.increment = increment

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.salary * (self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, value):
        # update base salary so that computed value becomes "value"
        self.salary = value / (1 + self.increment / 100)


emp = Employee()

print(emp.salaryAfterIncrement)  # computed value

emp.salaryAfterIncrement = 10000  # updates salary

print(emp.salary)                # new salary
print(emp.salaryAfterIncrement)  # should match 10000