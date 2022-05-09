class Book:
    id = None
    title = None
    author = None
    year = None
    category = None

    def __init__(self, id, title, author, year, category):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.category = category


class Library:
    _libraries = []

    def __init__(self, *books):
        self.add(*books)

    def add(self, *books):
        for book in books:
            if not isinstance(book, Book):
                raise TypeError('Неверный тип данных!')
            self._libraries.append(book)

    def remove(self, id):
        book = next((x for x in self._libraries if x.id == id), None)
        if book is None:
            print('Книга не найдена!')
            return False
        self._libraries.remove(book)
        return True

    def print_library(self):
        print('Книги в библиотеке:')
        for book in self._libraries:
            print(book.id, book.title, book.author, book.year, book.category)

    @staticmethod
    def print_books(*books):
        print('Список книг:')
        for book in books:
            if not isinstance(book, Book):
                raise TypeError('Неверный тип данных!')
            print(book.id, book.title, book.author, book.year, book.category)

    def sorted(self, field):
        n = len(self._libraries)
        if n <= 1:
            return self._libraries
        if isinstance(getattr(self._libraries[0], field), int):
            for i in range(n - 1):
                for j in range(n - i - 1):
                    book_first, book_second = getattr(self._libraries[j], field), getattr(self._libraries[j + 1], field)
                    if book_first > book_second:
                        self._libraries[j], self._libraries[j + 1] = self._libraries[j + 1], self._libraries[j]
        elif isinstance(getattr(self._libraries[0], field), str):
            for i in range(n - 1):
                for j in range(n - i - 1):
                    book_first, book_second = getattr(self._libraries[j], field), getattr(self._libraries[j + 1], field)
                    min_size = len(book_first) if len(book_first) <= len(book_second) else len(book_second)
                    for char in range(min_size):
                        if book_first[char] > book_second[char]:
                            self._libraries[j], self._libraries[j + 1] = self._libraries[j + 1], self._libraries[j]
                            break
                        elif book_first[char] < book_second[char]:
                            break
        return self._libraries

    def find(self, **fields):
        response = self._libraries.copy()
        for field, value in fields.items():
            for book in response.copy():
                if not getattr(book, field) == value:
                    response.remove(book)
        return response
