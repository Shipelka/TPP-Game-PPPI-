class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.shield = 50
        self.currency = 0
        self.kills = 0
        self.deaths = 0
        self.assists = 0

    def take_damage(self, amount):
        if self.shield > 0:
            absorbed = min(amount, self.shield)
            self.shield -= absorbed
            amount -= absorbed
        self.hp -= amount
        if self.hp <= 0:
            self.die()

    def die(self):
        print(f"{self.name} has died.")

class NPC:
    def __init__(self, type, hp):
        self.type = type
        self.hp = hp

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            print(f"{self.type} defeated.")
