# @property = decorator used to define a method as a property( it can be accessed like an attribute)
# Benefit: add additional logic when read, write or delete attributes
 # gives you getter , setter, and deleter method. 


class Rectangle:
    def __init__(self, length, breadth):
        self._length = length
        self._breadth = breadth

    
    @property
    def breadth(self):
        return f'{self.breadth}cm'
    
    @property
    def length(self):
        return f'{self.length}cm'
    

    @length.setter
    def length(self, new_length):
        if new_length > 0:
            self._length = new_length
        else:
            print("length must be greater than 0")

    @breadth.setter
    def breadth(self, new_breadth):
        if new_breadth > 0:
            self._breadth = new_breadth
        else:
            print("length must be greater than 0")

rectange = Rectangle(20, 10)

rectange.breadth = 5

print(rectange.length)
print(rectange.breadth)



