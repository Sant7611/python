# class calculate:
#     def __init__(self, n):
#         self.n = n

#     def __add__(self, num):
#         return self.n + num.n

# n = calculate(1)
# m = calculate(2)

# print(n+m)


class Box:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        a =Box(self.a + other.a)
        return a
    
    def __str__(self):
        return str(self.a)
    
a = Box(5)
b = Box(10)

c = a+b

print(c.a)

class Calc:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        m3 = Calc(m1,m2)
        return m3

m1 = Calc(10, 20)
m2 = Calc(20, 20)

m3 = m1 + m2
print(m3.m2)