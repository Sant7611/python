#super() keyword : used to extend the functionality of the inherited method . 
# this is also used to call the parent methods.

class Shapes:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f'this is {self.is_filled}. and {self.color} in color')


class Circle(Shapes):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

        #this is method overriding
    def describe(self):
        print(f'The area of this shape is {3.14 *self.radius *self.radius}')
        super().describe()

class Square(Shapes):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width


circle = Circle('red', True, 5)
square = Square('blue', False, 9)
print(circle.color)
print(square.is_filled, square.width)
circle.describe()