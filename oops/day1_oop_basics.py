# Day 1: Demystifying OOP (Object Oriented Programming)

# 1. Classes vs Objects
# Think of a Class as a blueprint for a house.
# Think of an Object as the actual house built from that blueprint.
# You can build many houses (Objects) from one blueprint (Class).

class Car:
    # 2. __init__ (The Constructor)
    # This acts as the setup function. The moment you create a new Car object,
    # python perfectly runs this function to set the initial values.
    
    def __init__(self, brand, color):
        # 3. self (Who are we talking about?)
        # 'self' means "this specific object". 
        # So "self.brand = brand" means "set the brand of THIS SPECIFIC car to the brand passed in."
        self.brand = brand
        self.color = color
        
        # 4. Encapsulation (Hiding data)
        # Sometimes you don't want the outside world messing with internal settings.
        # Adding two underscores before a variable name makes it "private".
        self.__engine_status = "Off" 

    # We can create functions inside a class, known as "Methods"
    def start_engine(self):
        self.__engine_status = "On"
        print(f"The {self.color} {self.brand}'s engine is now {self.__engine_status}!")

    def get_engine_status(self):
        # We use this to safely check the private variable
        return self.__engine_status

# --- Let's put the Blueprint to use! ---

# We are creating two separate Objects (instances) from the Car class.
car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

# Let's test them out!
print(f"Car 1 is a {car1.color} {car1.brand}")
print(f"Car 2 is a {car2.color} {car2.brand}")

car1.start_engine()

# Trying to access a private variable directly will cause an error!
# print(car1.__engine_status) # Uncommenting this line will crash the program.

# Safe way to check private status:
print(f"Checking engine status safely: {car1.get_engine_status()}")




class BankAccount():
    def __init__(self, holder_name):
        self.holder_name = holder_name

        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance +=amount

            print(f"Your balance is credited by rs.{amount} ")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f'your balance has been deducted by {amount}')

    def getbalance(self):
        return self.__balance
    
holder1 = BankAccount('santosh bohara')
print(holder1.getbalance())
holder1.deposit(5000)
holder1.withdraw(2000)
print(holder1.getbalance())

