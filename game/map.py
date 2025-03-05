class Map:
    def __init__(self, name):
        self.name = name
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def display(self):
        print(f"Map: {self.name}, Objects: {len(self.objects)}")
