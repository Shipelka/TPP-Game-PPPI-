class Map:
    def __init__(self, name):
        self.name = name
        self.objects = []

    def add_object(self, obj):
        """Добавляет объект на карту."""
        self.objects.append(obj)

    def remove_object(self, obj):
        """Удаляет объект с карты."""
        if obj in self.objects:
            self.objects.remove(obj)
            print(f"{obj} removed from the map.")
        else:
            print(f"{obj} not found on the map.")

    def display(self):
        """Отображает информацию о карте и её объектах."""
        print(f"Map: {self.name}")
        print(f"Objects on the map: {len(self.objects)}")
        for obj in self.objects:
            print(f"- {obj}")

    def clear(self):
        """Очищает карту от всех объектов."""
        self.objects.clear()
        print("The map has been cleared.")

    def find_object(self, obj_name):
        """Ищет объект по имени."""
        for obj in self.objects:
            if obj.name == obj_name:
                return obj
        return None
