class Employee:  #this is class
    name = 'santosh'
    salary = 100000
    def greet(self):
        print(f'Hello, {self.name}')


hari = Employee()
hari.greet()

#the line 9 converts into line 12 while executing.
Employee.greet(hari)  #meaning that self should be used to point to that particular object.
