from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Your car is starting")

    def stop(self):
        print("Your car is stopping")

car1 = Car()
car1.start()