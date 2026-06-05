class Programmer:
    company = 'microsoft'
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

    
p = Programmer('Santosh', 1200000, 12421)
print(p.company, p.name, p.salary, p.pincode)