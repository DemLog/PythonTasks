import enum
import json
from pathlib import Path

from polynomial import Polynomial

from animals import Predatory, Omnivorous, Herbivorous, Animal
from food import Meaty, Vegetable

from libraries import Book, Library


def polynomial_test():
    a = Polynomial(1, 2, 3, 4, 5)
    b = Polynomial(6, 7, 8)
    print("A: {0}".format(a))
    print("B: {0}".format(b))
    print("Сложение A + B: {0}".format(a + b))
    print("Вычитание A - B: {0}".format(a - b))
    print("Умножение A * B: {0}".format(a * b))
    print("Значение многочлена A от x=2: {0}".format(a.calculate(2)))


def animals_test():
    def print_animals(arr):
        print('Список животных:')
        for item in arr:
            print(item.display_animal())

    def print_animals_tag(arr, a_type, end, start=0):
        print('Список животных по тегу {0}:'.format(a_type))
        for item in range(start, end):
            print(getattr(arr[item], a_type))

    def ordering(arr):
        n = len(arr)
        result = arr.copy()
        for i in range(n - 1):
            for j in range(n - i - 1):
                if result[j].count_food < result[j + 1].count_food:
                    result[j], result[j + 1] = result[j + 1], result[j]
                elif result[j].count_food == result[j + 1].count_food:
                    size = len(result[j].name) if len(result[j].name) <= len(result[j + 1].name) else len(
                        result[j + 1].name)
                    for char in range(size):
                        if result[j].name[char] > result[j + 1].name[char]:
                            result[j], result[j + 1] = result[j + 1], result[j]
                            break
                        elif result[j].name[char] < result[j + 1].name[char]:
                            break

        return result

    def write_file(arr, path='animals.json'):
        if not Path(path).suffix == '.json':
            raise FileExistsError('Неверный формат файла! Нужен json.')

        with open(path, "w", encoding='utf8') as f:
            for item in arr:
                type_food = item.type_food
                response = {
                    'classname': item.__class__.__name__,
                    'id': item.id,
                    'name': item.name,
                    'type_food': {'classname': type_food.__class__.__name__, 'name': type_food._name_},
                    'count_food': item.count_food
                }
                f.write(json.dumps(response, ensure_ascii=False) + '\n')

    def read_file(path='animals.json'):
        if not Path(path).suffix == '.json':
            raise FileExistsError('Неверный формат файла! Нужен json.')

        response = []
        with open(path, "r", encoding='utf8') as f:
            for item in f:
                animal_json = json.loads(item)
                type_animal = Animal
                type_food = enum.Enum
                for cls in Animal.__subclasses__():
                    if animal_json["classname"] == cls.__name__:
                        type_animal = cls
                for cls in enum.Enum.__subclasses__():
                    if animal_json["type_food"]["classname"] == cls.__name__:
                        type_food = cls
                try:
                    type_food = getattr(type_food, animal_json["type_food"]["name"])
                    animal = type_animal(id_animal=animal_json["id"], name=animal_json["name"], type_food=type_food,
                                         count_food=animal_json["count_food"])
                    response.append(animal)
                except Exception:
                    print('Невозможно декодировать строку: {0}'.format(animal_json))
        return response

    animals = [
        Predatory(id_animal=0, name='Тигр', type_food=Meaty.beef, count_food=4),
        Predatory(id_animal=1, name='Волк', type_food=Meaty.beef, count_food=3),
        Omnivorous(id_animal=2, name='Корова', type_food=Vegetable.grass, count_food=10),
        Omnivorous(id_animal=3, name='Заяц', type_food=Vegetable.carrot, count_food=6),
        Herbivorous(id_animal=4, name='Человек', type_food=Meaty.fish, count_food=3),
        Herbivorous(id_animal=5, name='Медведь', type_food=Vegetable.corn, count_food=8),
        Animal(id_animal=6, name='Кот', type_food=Meaty.fish, count_food=4)
    ]

    write_file(animals)
    animals_file = read_file()
    order = ordering(animals_file)
    print_animals(order)
    print_animals_tag(order, 'name', 5)
    print_animals_tag(order, 'id', len(order), len(order) - 3)


def libraries_test():
    lib = Library(
        Book(13, 'Маракотова бездна', 'Артур Конан Дойл', 1929, 'Фантастика'),
        Book(245, 'Искусство сновидения', 'Карлос Кастанеда', 1993, 'Философия'),
        Book(2, 'Рыцарь на золотом коне', 'Диана Уинн Джонс', 1985, 'Детская литература'),
        Book(76, 'В зоне тумана', 'Алексей Гравицкий', 2009, 'Фантастика'),
        Book(34, 'Армагеддон', 'Роман Злотников', 2002, 'Фантастика'),
        Book(8, 'Конармия', 'Артур Конан Дойл', 1937, 'Книги о войне'),
        Book(55, 'Тонкое искусство пофигизма', 'Марк Мэнсон', 2016, 'Психология'),
        Book(123, 'Не позже полуночи', 'Дафна Дю Морье', 1971, 'Ужасы'),
        Book(754, 'Тихий Дон', 'Михаил Шолохов', 1940, 'Книги о войне')
    )

    lib.add(Book(132, 'Правда жизни', 'Грэм Джойс', 2002, 'Книги о войне'))
    lib.remove(34)
    lib.sorted('id')
    lib.print_library()
    find_books = lib.find(category='Фантастика')
    lib.print_books(*find_books)


if __name__ == '__main__':
    print('============== Тест многочлена ==============')
    polynomial_test()
    print('============== Тест класса животных ==============')
    animals_test()
    print('============== Тест библиотеки ==============')
    libraries_test()
