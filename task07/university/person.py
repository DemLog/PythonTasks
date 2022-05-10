from task07.university.exam import Rating


class Person:

    def __init__(self, fullname: str):
        self._last_name, self._first_name, self._patronymic = fullname.split(" ")

    def get_fullname(self):
        return " ".join([self._last_name, self._first_name, self._patronymic])

    def get_shortname(self):
        return "{0} {1}.{2}.".format(self._last_name, self._first_name[0], self._patronymic[0])


class Teacher(Person):

    def __init__(self, fullname: str, login: str, password: str):
        super(Teacher, self).__init__(fullname)
        self._login = login
        self._password = password

    def login_teacher(self, login: str, password: str):
        if not login == self._login:
            return False
        if not password == self._password:
            return False
        return self


class Enrollee(Person):

    def __init__(self, fullname: str):
        super().__init__(fullname)
        self._enrolled = False
        self.rating: Rating = Rating()

    def get_enrolled(self):
        return dict(
            msg="Зачислен" if self._enrolled else "Не зачислен",
            status=self._enrolled
        )

    def set_enrolled(self, status: bool):
        self._enrolled = status
