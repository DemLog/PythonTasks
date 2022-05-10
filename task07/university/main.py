from task07.university.exam import Exam
from task07.university.person import Enrollee, Teacher
from task07.university.university import Faculty


class System:
    # используется, как кэш
    enrollee: Enrollee = None
    teacher: Teacher = None
    faculty = Faculty("Математический факультет", Teacher("Иванов Иван Иванович", "admin", "admin"))

    def display_menu(self):
        print('\n| Меню системы сдачи вступительных экзаменов |')
        print('''
            1. Зарегистрироваться на факультете
            2. Панель управления преподавателя
            3. Пройти экзамен
            4. Информация о факультете
        ''')

    def select_menu(self, button):
        if button == 1:
            return self.register_enrollee()
        elif button == 2:
            self.display_teacher_menu()
            button = int(input('Выберите номер меню: '))
            self.select_teacher_menu(button)
        elif button == 3:
            pass
        elif button == 4:
            return self.show_info_faculty()
        else:
            print('ОШИБКА! Неправильно выбрана команда.')
            return False

    def register_enrollee(self):
        try:
            name = input('Введите Фамилию Имя Отчество (одной строкой, с пробелами): ')
            enrollee = Enrollee(name)
            return self.faculty.add_enrollee(enrollee)
        except ValueError:
            print('ОШИБКА! Неправильно введено имя.')
            return False

    def show_info_faculty(self):
        print(self.faculty.get_info())
        return True

    def display_teacher_menu(self):
        print('\n| Панель преподавателя |')
        print('''
            1. Авторизация преподавателя
            2. Управление факультетом
            3. Проверить работы абитуриентов
        ''')

    def select_teacher_menu(self, button):
        if button == 1:
            return self.login_teacher()
        elif button == 2:
            if self.teacher is None:
                print('ОШИБКА! Для начала войдите в систему.')
                return False
            self.display_faculty_menu()
            button = int(input('Выберите номер меню: '))
            self.select_faculty_menu(button)
        elif button == 3:
            if self.teacher is None:
                print('ОШИБКА! Для начала войдите в систему.')
                return False
        else:
            print('ОШИБКА! Неправильно выбрана команда.')
            return False

    def display_faculty_menu(self):
        print('\n| Панель управления факультетом |')
        print('''
                1. Список абитуриентов
                2. Удалить абитуриента
                3. Добавить экзамен
                4. Удалить экзамен
                5. Список экзаменов
                6. Изменить количество бюджетных мест
        ''')

    def select_faculty_menu(self, button):
        if button == 1:
            return self.show_enrollees()
        elif button == 2:
            return self.remove_enrollee()
        elif button == 3:
            return self.create_exam()
        elif button == 4:
            return self.remove_exam()
        elif button == 5:
            return self.show_exams()
        elif button == 6:
            try:
                count = int(input('Введите количество бюджетных мест: '))
                self.faculty.change_places(count, self.teacher)
            except ValueError:
                print('ОШИБКА! Неправильно введены данные.')
                return False
        else:
            print('ОШИБКА! Неправильно выбрана команда.')
            return False

    def create_exam(self):
        name = input('Введите название экзамена: ')
        try:
            exam = Exam(name)
            while True:
                question = input('Введите вопрос для экзамена (для выхода нажмите Enter): ')
                if len(question) == 0:
                    break
                exam.add(question)
            print('В экзамене "{0}" содержится {1} вопросов.'.format(name, len(exam.get_questions())))
            return self.faculty.add_exam(exam, self.teacher)
        except ValueError:
            print('ОШИБКА! Неправильно введены данные.')
            return False

    def login_teacher(self):
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        try:
            _teacher = self.faculty.get_teacher().login_teacher(login, password)
            if not _teacher:
                raise ValueError()
            print('Вы успешно вошли в систему!')
            self.teacher = _teacher
            return True
        except ValueError:
            print('ОШИБКА! Неправильно введены данные.')
            return False

    def show_enrollees(self):
        print('Список абитуриентов:')
        for index, value in enumerate(self.faculty.get_enrollees(self.teacher)):
            print(". ".join([index + 1, value.get_fullname()]))

    def show_exams(self):
        print('Список экзаменов:')
        for exam in self.faculty.get_exams(self.teacher):
            print(". ".join([str(exam.id + 1), exam.get_name()]))

    def remove_enrollee(self):
        self.show_enrollees()
        try:
            id = int(input('Выберите номер абитуриента (0 для выхода): '))
            if id == 0:
                return False
            _enrollee = self.faculty.get_enrollees()[id - 1]
            return self.faculty.remove_enrollee(_enrollee)
        except IndexError:
            print('ОШИБКА! Неправильно введен ID.')
            return False
        except ValueError:
            print('ОШИБКА! Неправильно введены данные.')
            return False

    def remove_exam(self):
        self.show_exams()
        try:
            id = int(input('Выберите номер экзамена (0 для выхода): '))
            if id == 0:
                return False
            _exam = self.faculty.get_exam(id + 1)
            return self.faculty.remove_exam(_exam, self.teacher)
        except IndexError:
            print('ОШИБКА! Неправильно введен ID.')
            return False
        except ValueError:
            print('ОШИБКА! Неправильно введены данные.')
            return False


if __name__ == '__main__':
    test = System()
    while True:
        test.display_menu()
        button = int(input('Выберите номер меню: '))
        test.select_menu(button)
