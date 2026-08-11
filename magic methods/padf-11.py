class player:
    def __init__(self,name,health,attack_power):
        self.name=name
        self.health=health
        self.attack_power=attack_power
    def attack(self,enemy):
        enemy.health-=self.attack_power
        return enemy.health
    def __str__(self):
        return f"game name:{self.name},health:{self.health},attack power{self.attack_power}"
a=player("temple-run",100,25)
b=player("surway:",80,35)
print(a)
print("-"*12)
print(b)
a.attack(b)
b.attack(a)
print(b.health)
print(a.health)
