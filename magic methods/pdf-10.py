# Question 10: Game Player
# Create a class Player with:
# •	attributes: name, health, attack_power 
# •	method: attack(enemy) 
# Implement:
# •	__str__() 
# •	__add__() → combine attack powers 
# •	__sub__() → reduce health after attack 
# •	__gt__() → compare health 
# •	__eq__() → compare attack power 
class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, enemy):
        enemy.health -= self.attack_power

    def __str__(self):
        return f"Name: {self.name}, Health: {self.health}, Attack Power: {self.attack_power}"

    def __add__(self, other):
        return self.attack_power + other.attack_power

    def __sub__(self, other):
        return self.health - other.health

    def __gt__(self, other):
        return self.health > other.health

    def __eq__(self, other):
        return self.attack_power == other.attack_power
a = Player("Alice", 100, 20)
b = Player("Bob", 80, 25)
print(a)
print("-"*13)
print(b)
print("-"*13)
a.attack(b)
print(f"After attack, Bob's health: {b.health}")
print(f"Combined attack power: {a + b}")
print(f"Health difference: {a - b}")
print(f"Is Alice healthier than Bob? {'Yes' if a > b else 'No'}")
print(f"Do Alice and Bob have the same attack power? {'Yes' if a == b else 'No'}")