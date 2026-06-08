#write a class vector representing a vector of 3 dimensions. overload the + and * opertaor which calculates the sum and the dot(.) product of them.

class Vector:

    def __init__(self, x, y ,z):
        self.x= x
        self.y= y
        self.z= z
        
    def __add__(self, other):
        x = self.x +other.x 
        y=self.y +other.y
        z = self.z +other.z
        return Vector(x,y,z)
    
    def __mul__(self,other):
        res = self.x *other.x +self.y *other.y +self.z *other.z 
        return (res)
    
    def __str__(self):
        return f'{self.x}i + {self.y}j + {self.z}k'

v1 = Vector(1,2,3)
v2 = Vector(2,3,4)

v3 = v1 + v2
# print(v3.x, v3.y, v3.z)
print(v3)
 
m3 = v1 * v2
print(m3)