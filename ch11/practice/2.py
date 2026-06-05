class Calculator:
    def __init__(self, num1):
        self.num1 = num1

    
    def square(self):
        return self.num1*self.num1
    

    def cube(self):
        return self.num1 * self.num1 * self.num1
    
    def square_root(self):
        return self.num1**1/2
    

square = Calculator(4)
print(square.square())

cube = Calculator(4)
print(cube.cube())

square_root = Calculator(4)
print(square_root.square_root())