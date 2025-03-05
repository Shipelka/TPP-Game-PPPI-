import time

class GameLoop:
    def __init__(self):
        self.running = True

    def start(self):
        print("Game started.")
        while self.running:
            self.update()
            time.sleep(0.016)  # ~60 FPS

    def update(self):
        print("Updating game state...")
        # Обновление логики игры

    def stop(self):
        self.running = False
        print("Game stopped.")
