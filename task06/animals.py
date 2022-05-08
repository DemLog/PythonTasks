from food import Meaty, Vegetable


class Animal:
    id = 0
    name = ''
    type_food = None
    count_food = 0

    def __init__(self, id_animal, name, type_food, count_food):
        self.id = id_animal
        self.name = name
        self.type_food = type_food
        self.count_food = count_food

    def display_food(self):
        return "[{0}] Тип пищи: {1} | Кол-во пищи: {2}".format(self.name, self.type_food.value, self.count_food)

    def display_animal(self):
        return "ID: {0} | Имя: {1} | Тип пищи: {2} | Кол-во пищи: {3}".format(self.id, self.name,
                                                                              self.type_food.value,
                                                                              self.count_food)


class Predatory(Animal):
    def __init__(self, **kwargs):
        if not isinstance(kwargs['type_food'], Meaty):
            raise TypeError("Неверный тип пищи для данного животного!")
        super().__init__(**kwargs)


class Omnivorous(Animal):
    def __init__(self, **kwargs):
        if not isinstance(kwargs['type_food'], Vegetable):
            raise TypeError("Неверный тип пищи для данного животного!")
        super().__init__(**kwargs)


class Herbivorous(Animal):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
