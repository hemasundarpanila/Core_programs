# Question 9: Laptop Specification
# Create a class Laptop with:
# •	attributes: brand, ram, price 
# •	method: upgrade_ram(extra_ram) 
# Implement:
# •	__str__() 
# •	__add__() → add prices of two laptops 
# •	__mul__() → multiply price for bulk purchase 
# •	__lt__() → compare price 
# •	__eq__() → compare RAM 
class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price

    def upgrade_ram(self, extra_ram):
        self.ram += extra_ram

    def __str__(self):
        return f"Brand: {self.brand}, RAM: {self.ram}GB, Price: ${self.price}"

    def __add__(self, other):
        return self.price + other.price

    def __mul__(self, quantity):
        return self.price * quantity

    def __lt__(self, other):
        return self.price < other.price

    def __eq__(self, other):
        return self.ram == other.ram
a = Laptop("Dell", 8, 800)
b = Laptop("HP", 16, 1200)
print(a)
print("-"*13)
print(b)
print("-"*13)
a.upgrade_ram(4)
print(f"Upgraded RAM for Dell laptop: {a.ram}GB")
print(f"Total price for both laptops: ${a + b}")
print(f"Bulk purchase price for 2 Dell laptops: ${a * 2}")