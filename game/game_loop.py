import time

class GameLoop:
    """
    Класс, реализующий главный игровой цикл.

    Атрибуты:
        running (bool): Флаг, указывающий на то, запущена ли игра (по умолчанию False).
        target_fps (int): Целевая частота кадров (по умолчанию 60).
        last_time (float): Время последнего кадра.
        frame_count (int): Счётчик кадров.
        elapsed_time (float): Время, прошедшее с последнего расчёта FPS.

    Методы:
        start(): Запуск игрового цикла, обновление логики игры, обработка событий, отрисовка.
        update(): Обновление состояния игры.
        handle_events(): Обработка событий (например, нажатие клавиш, движения мыши).
        render(): Отображение состояния игры (например, отрисовка на экране).
        stop(): Остановка игрового цикла.
    """

    def __init__(self, target_fps=60):
        """
        Инициализация игрового цикла.

        Аргументы:
            target_fps (int): Целевая частота кадров (по умолчанию 60).
        """
        self.running = False
        self.target_fps = target_fps
        self.last_time = time.time()
        self.frame_count = 0
        self.elapsed_time = 0

    def start(self):
        """
        Запуск игрового цикла. В этом методе происходит основное обновление игры:
        - Обновление логики.
        - Обработка событий.
        - Отображение состояния игры.
        Также рассчитывается FPS и контролируется частота кадров.
        """
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
        """
        Обновление логики игры, вызов этого метода происходит каждый кадр.
        Здесь можно обновлять позиции объектов, проверять коллизии, изменять состояния игры.
        """
        print("Updating game state...")

    def handle_events(self):
        """
        Обработка событий, таких как нажатие клавиш, движение мыши и другие действия игрока.
        Этот метод вызывается каждый кадр.
        """
        print("Handling events...")

    def render(self):
        """
        Отрисовка игрового состояния. Здесь происходит вывод на экран (например, отрисовка объектов, интерфейса).
        Этот метод вызывается каждый кадр.
        """
        print("Rendering game state...")

    def stop(self):
        """
        Остановка игрового цикла. Устанавливает флаг running в False, что прекращает работу игры.
        """
        self.running = False
        print("Game stopped.")
