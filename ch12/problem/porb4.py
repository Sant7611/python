#create a class Complex to represent complex numbers, along with overloaded operatros '+' and '*' which adds and multiplies them.

# class Complex:
#     def __init__(self, r, i):
#         self.r = r 
#         self.i = i

#     def __add__(self, c2):
#         r = self.r + c2.r
#         i = self.i + c2.i
#         return Complex(r, i)
    
#     # def __str__(self):
#     #     return f'{self.r}+ {self.i}i'

# c1 = Complex(1,2)
# c2 = Complex(2,3)

# c3 = c1 + c2
# print(f'{c3.r} + {c3.i}i')


class Complex:
    def __init__(self, r, i):
        self.r = r 
        self.i = i

    # addition
    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    # multiplication
    def __mul__(self, other):
        r = self.r * other.r - self.i * other.i
        i = self.r * other.i + self.i * other.r
        return Complex(r, i)


c1 = Complex(1, 2)
c2 = Complex(2, 3)

c3 = c1 + c2
c4 = c1 * c2

print(f"{c3.r} + {c3.i}i")
print(f"{c4.r} + {c4.i}i")