import random


class CustomArray:
    _array = []
    _size_arr = 0

    def __init__(self, size_arr):
        self._size_arr = size_arr

    def __del__(self):
        pass

    def __getitem__(self, item):
        if item > self._size_arr - 1:
            raise IndexError("Нет такого элемента!")
        return self._array[item]

    def __setitem__(self, key, value):
        if key > self._size_arr - 1:
            raise IndexError("Нет такого элемента!")
        self._array[key] = value
        return True

    def shuffle_arr(self):
        if self._size_arr <= 1:
            return self._array

        # Более упрощенная форма:
        # random.shuffle(self._array)
        # return self._array
        for i in range(self._size_arr):
            rnd = random.randint(0, self._size_arr - 1)
            first_val, second_val = self._array[rnd], self._array[rnd - 1]
            self._array[rnd - 1], self._array[rnd] = first_val, second_val
        return self._array

    def find_unique_elements(self):
        empty_list = []
        for item in self._array:
            if item not in empty_list:
                empty_list.append(item)

        return empty_list

    def print_console_arr(self):
        print(self._array)
        return True


class NumberArr(CustomArray):
    MAX_RND_NUMBER = 100000

    def __init__(self, size_arr):
        super().__init__(size_arr)
        self._array = [0] * size_arr

    def set_rnd_int(self, max_range=MAX_RND_NUMBER):
        for i in range(self._size_arr):
            self._array[i] = random.randint(0, max_range)
        return self._array


class StringArr(CustomArray):

    def __init__(self, size_arr, arr=[]):
        super().__init__(size_arr)
        if not len(arr) == size_arr and len(arr) > 0:
            raise IndexError("Размер задаваемого массива не совпадает с массивом элементов!")
        elif len(arr) == size_arr:
            if any(not self._check_string(item) for item in arr):
                raise TypeError("Массив состоит не полностью из строк!")
            self._array = arr
        else:
            self._array = [""] * size_arr

    def __setitem__(self, key, value):
        if key > self._size_arr - 1:
            raise IndexError("Нет такого элемента!")
        if not type(value) == "string":
            raise TypeError("Требуемый тип не String!")

        self._array[key] = value
        return True

    def __add__(self, other: CustomArray):
        result = self._array.copy()
        size_arr = self._size_arr + other._size_arr

        for item in other:
            result.append(item)
        return StringArr(size_arr, result)

    def merge_unique(self, arr: CustomArray):
        empty_list = self.find_unique_elements()

        for item in arr.find_unique_elements():
            if item not in empty_list:
                empty_list.append(item)

        self.__init__(len(empty_list), empty_list)
        return True

    @staticmethod
    def _check_string(value):
        return isinstance(value, str)
