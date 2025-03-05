import time

class GameLoop:
    def __init__(self, target_fps=60):
        self.running = False
        self.target_fps = target_fps
        self.last_time = time.time()
        self.frame_count = 0
        self.elapsed_time = 0

    def start(self):
        self.running = True
        self.last_time = time.time()  # Сброс времени
        print("Game started.")
        while self.running:
            start_frame_time = time.time()

            self.update()  # Обновление логики игры
            self.handle_events()  # Обработка событий
            self.render()  # Отображение (например, отрисовка)

            self.frame_count += 1
            self.elapsed_time += time.time() - self.last_time
            self.last_time = start_frame_time

            # Подсчёт FPS
            if self.elapsed_time >= 1.0:
                fps = self.frame_count / self.elapsed_time
                print(f"FPS: {fps:.2f}")
                self.frame_count = 0
                self.elapsed_time = 0

            # Ожидание, чтобы поддержать целевой FPS
            time_to_sleep = max(0, (1.0 / self.target_fps) - (time.time() - start_frame_time))
            time.sleep(time_to_sleep)

    def update(self):
        """Обновление логики игры"""
        print("Updating game state...")

    def handle_events(self):
        """Обработка пользовательских событий"""
        print("Handling events...")

    def render(self):
        """Отрисовка/вывод на экран"""
        print("Rendering game state...")

    def stop(self):
        self.running = False
        print("Game stopped.")
