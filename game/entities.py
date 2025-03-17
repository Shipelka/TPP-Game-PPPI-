class Player:
    """
    Класс, представляющий игрока.

    Атрибуты:
        name (str): Имя игрока.
        hp (int): Количество здоровья игрока (по умолчанию 100).
        shield (int): Количество щита игрока (по умолчанию 50).
        currency (int): Количество валюты игрока (по умолчанию 0).
        kills (int): Количество убийств игрока (по умолчанию 0).
        deaths (int): Количество смертей игрока (по умолчанию 0).
        assists (int): Количество помощи игрока (по умолчанию 0).

    Методы:
        take_damage(amount): Игрок принимает урон. Урон сначала поглощается щитом, если он есть, затем уходит на здоровье.
        die(): Игрок умирает и выводится сообщение о смерти.
    """

    def __init__(self, name):
        """
        Инициализация игрока.

        Аргументы:
            name (str): Имя игрока.
        """
        self.name = name
        self.hp = 100
        self.shield = 50
        self.currency = 0
        self.kills = 0
        self.deaths = 0
        self.assists = 0

    def take_damage(self, amount):
        """
        Игрок принимает урон. Если у него есть щит, то он поглощает часть урона.

        Аргументы:
            amount (int): Количество урона, которое игрок должен получить.
        """
        if self.shield > 0:
            absorbed = min(amount, self.shield)
            self.shield -= absorbed
            amount -= absorbed
        self.hp -= amount
        if self.hp <= 0:
            self.die()

    def die(self):
        """
        Метод, вызываемый, когда здоровье игрока падает до нуля. Выводится сообщение о смерти.
        """
        print(f"{self.name} has died.")


class NPC:
    """
    Класс, представляющий неигрового персонажа (NPC).

    Атрибуты:
        type (str): Тип NPC.
        hp (int): Количество здоровья NPC.

    Методы:
        take_damage(amount): NPC принимает урон. Когда его здоровье падает до нуля, NPC считается побежденным.
    """

    def __init__(self, type, hp):
        """
        Инициализация NPC.

        Аргументы:
            type (str): Тип NPC.
            hp (int): Количество здоровья NPC.
        """
        self.type = type
        self.hp = hp

    def take_damage(self, amount):
        """
        NPC принимает урон. Если его здоровье падает до нуля, NPC побежден.

        Аргументы:
            amount (int): Количество урона, которое NPC должен получить.
        """
        self.hp -= amount
        if self.hp <= 0:
            print(f"{self.type} defeated.")
