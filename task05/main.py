from customArray import NumberArr, StringArr


def test_number_array():
    test = NumberArr(50)
    print("Создан экземпляр класса NumberArr")
    test.print_console_arr()
    test.set_rnd_int(100)
    print("Добавлены рандомные значения")
    test.print_console_arr()
    test.shuffle_arr()
    print("Значения перемешаны")
    test.print_console_arr()
    print("Количество уникальный значений: {0}".format(len(test.find_unique_elements())))


def test_string_array():
    first_arr = ["ананас", "апельсин", "банан", "яблоко", "груша", "банан", "ананас", "штанга", "мяч"]
    second_arr = ["мяч", "обруч", "штанга", "часы", "яблоко", "ананас", "газон", "мяч"]

    test_1 = StringArr(len(first_arr), first_arr)
    print("Создан экземпляр №1 класса StringArray")
    test_1.print_console_arr()
    test_2 = StringArr(len(second_arr), second_arr)
    print("Создан экземпляр №2 класса StringArray")
    test_2.print_console_arr()
    print("Четвертый элемент массива: {0}".format(test_1[3]))
    test_3 = test_1 + test_2
    print("Конкатенация двух массивов")
    test_3.print_console_arr()
    print("Слияние двух массивов")
    test_1.merge_unique(test_2)
    test_1.print_console_arr()


if __name__ == '__main__':
    test_number_array()
    print('\n')
    test_string_array()
