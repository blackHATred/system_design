from random import randint


class Item:
    def __init__(self, name: str, description: str):
        self.id = randint(1, 100000)
        self.name = name
        self.description = description
        # тут должна быть 3д моделька
        self.model = "нюхаем цветоч и никакова стресса"
