class Animal:
    pass


class Pets(Animal):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("This dog barks.")


d = Dog()
d.bark()