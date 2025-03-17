class Menu:
    """
    Класс, представляющий главное меню игры.

    Атрибуты:
        options (list): Список доступных опций в меню.

    Методы:
        display(): Выводит главное меню с доступными опциями.
        select_option(choice): Обрабатывает выбор пользователя и выполняет соответствующее действие.
    """

    def __init__(self):
        """
        Инициализация главного меню с предопределенными опциями:
            1. Start Game - Запуск игры
            2. Settings - Настройки
            3. Exit - Выход из игры
        """
        self.options = ["Start Game", "Settings", "Exit"]

    def display(self):
        """
        Выводит главное меню на экран.

        Пример вывода:
            Main Menu:
            1. Start Game
            2. Settings
            3. Exit
        """
        print("Main Menu:")
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")

    def select_option(self, choice):
        """
        Обрабатывает выбор пользователя и выполняет соответствующее действие.

        Аргументы:
            choice (int): Номер выбранной опции.

        Возможные варианты:
            1 - Запуск игры
            2 - Открытие настроек
            3 - Выход из игры
            Любое другое число - Ошибка (некорректный выбор)
        """
        if choice == 1:
            print("Starting game...")
        elif choice == 2:
            print("Opening settings...")
        elif choice == 3:
            print("Exiting game...")
        else:
            print("Invalid option.")
