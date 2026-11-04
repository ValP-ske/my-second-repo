import random
class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.attack_power = random.randint(3, 9)

    def attack(self, other):
        other.hp -= self.attack_power
        print(f"{self.name} attacks {other.name} for {self.attack_power} damage!")

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name}: {self.hp} HP"
