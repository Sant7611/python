
from abc import ABC, abstractmethod


class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14 *self.radius**2
    

class Square(Shape):
    def __init__(self,width):
        self.width = width
    
    def area(self):
        return self.width**2
    


class Triange(Shape):
    def __init__(self,base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return self.base * self.height * 0.5
    


class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping



shapes = [Circle(6), Square(5), Triange(6,7), Pizza('pepporeni', 7)]

for shape in shapes:
    print(f"The area is {shape.area()} cm2")