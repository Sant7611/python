

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof")


class Cat(Animal):
    def speak(self):
        print("meow")

class Car:
    alive = False
    def speak(self):
        print("HOnk")

class Mouse(Animal):
    def speak(self):
        print("Squeak")

animals = [Dog(), Cat(), Mouse(), Car()]
for i in animals:
    print(i.speak())
    print(i.alive)