import random
class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(30, 90)/100
        other.hp -= self.attack_power*damage
        print(f"{self.name} attacks {other.name} for {self.attack_power*damage:.2f} damage!")

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name}: {self.hp:.2f} HP"
