class HUD:
    def __init__(self, player):
        self.player = player

    def display(self):
        print(f"HP: {self.player.hp} | Shield: {self.player.shield} | Currency: {self.player.currency}")
        print(f"Kills: {self.player.kills} | Deaths: {self.player.deaths} | Assists: {self.player.assists}")

    def update(self):
        # Логика обновления HUD
        pass
