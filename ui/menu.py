class Menu:
    def __init__(self):
        self.options = ["Start Game", "Settings", "Exit"]

    def display(self):
        print("Main Menu:")
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")

    def select_option(self, choice):
        if choice == 1:
            print("Starting game...")
        elif choice == 2:
            print("Opening settings...")
        elif choice == 3:
            print("Exiting game...")
        else:
            print("Invalid option.")
