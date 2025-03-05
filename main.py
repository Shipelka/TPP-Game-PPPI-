from game.game_loop import GameLoop
from game.entities import Player, NPC
from game.map import Map
from ui.menu import Menu
from ui.hud import HUD
from localization.lang_detector import LanguageDetector
from networking.client import GameClient

def main():
    # Инициализация игры
    menu = Menu()
    menu.display()
    choice = int(input("Choose an option: "))
    menu.select_option(choice)

    if choice == 1:
        # Инициализация игрока
        player_name = input("Enter player name: ")
        player = Player(player_name)

        # Инициализация карты и объектов
        game_map = Map("World Map")
        npc = NPC("Goblin", 50)
        game_map.add_object(npc)
        game_map.display()

        # Инициализация HUD
        hud = HUD(player)

        # Инициализация игрового цикла
        game_loop = GameLoop()
        game_loop.start()

        # Инициализация сетевого клиента (для многопользовательской игры)
        client = GameClient()
        client.connect()
        
        # Инициализация детектора языка
        lang_detector = LanguageDetector()
        lang_code = lang_detector.detect("Hello, World!")
        lang_detector.set_language(lang_code)

        # Игровой процесс
        while True:
            # Обновление HUD
            hud.display()

            # Пример взаимодействия с игроком
            action = input("Enter an action (attack, heal, quit): ").lower()
            if action == "attack":
                npc.take_damage(10)
            elif action == "heal":
                player.take_damage(-10)
            elif action == "quit":
                game_loop.stop()
                break
            else:
                print("Invalid action.")

            # Дополнительные обновления
            game_loop.update()

if __name__ == "__main__":
    main()
