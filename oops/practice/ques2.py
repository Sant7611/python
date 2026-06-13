# 2. Composition (Building Systems from Parts)
# Real-world use case: "Composition over Inheritance" is a golden rule in modern software design to prevent deeply nested, fragile class hierarchies.

# The Scenario: An e-commerce checkout block.
# The Task:
# Create a Product class with name and price attributes.
# Create a ShoppingCart class. It shouldn't inherit from anything, but it should contain a list to hold items.
# Add methods to ShoppingCart to:
# add_item(product): Appends a Product object.
# get_total(): Loops through the products and returns the total price.
# Bonus: Add an __str__ magic method to ShoppingCart so print(cart) outputs something clean like: "Cart has 3 items. Total: $45.00".

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        cart_item = Product(name, price)
        self.items.append(cart_item)

    def get_total(self):
        total = 0
        for i in self.items:
            total += i.price
        return total

    def __str__(self):
        return f'The cart has {len(self.items)} items. The total is {self.get_total()}'

# product = Product('apple', 135)
cart = ShoppingCart()

cart.add_item('apple', 150)
cart.add_item('banana', 100)
cart.add_item('orange', 80)

print(cart.get_total())

print(cart)