class Employee():
    language = 'python'
    salary = 10000

    def __init__(self, name, salary, language): #dunder method. starts with __ calls automatically 
        self.name = name
        self.salary = salary
        self.language = language
        print("This is a dunder method. also known as constructor. calls automatically ")


emp1 = Employee('Santosh', 100000, 'python')

print(emp1.name, emp1.salary, emp1.language)