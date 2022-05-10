from task07.university.exam import Exam
from task07.university.person import Teacher, Enrollee


class Faculty:

    def __init__(self, name: str, teacher: Teacher = None):
        self._name = name
        self._teacher: Teacher = teacher
        self._enrollees: list[Enrollee] = []
        self._exams: list[Exam] = []
        self._count_place = 0

    def set_teacher(self, teacher: Teacher):
        if self._teacher is not None:
            print('На факультете {0} заменен преподаватель {1} на {2}'.format(self.get_name(),
                                                                              self._teacher.get_shortname(),
                                                                              teacher.get_shortname()))
        self._teacher = teacher

    def get_teacher(self):
        return self._teacher

    def get_name(self):
        return self._name

    def get_enrollees(self, teacher: Teacher):
        if teacher is not self._teacher:
            print('ОШИБКА! У вас нет прав доступа.')
            return False
        return self._enrollees

    def add_enrollee(self, enrollee: Enrollee):
        if enrollee in self._enrollees:
            print('ОШИБКА! Данный абитуриент уже зарегистрирован на факультете.')
            return False
        self._enrollees.append(enrollee)
        return True

    def remove_enrollee(self, enrollee: Enrollee):
        if enrollee not in self._enrollees:
            print('ОШИБКА! Данный абитуриент не зарегистрирован на факультете.')
            return False
        self._enrollees.remove(enrollee)
        del enrollee
        return True

    def add_exam(self, exam: Exam, teacher: Teacher):
        if teacher is not self._teacher:
            print('ОШИБКА! У вас нет прав доступа.')
            return False
        if exam in self._exams:
            print('ОШИБКА! Экзамен уже добавлен для прохождения.')
            return False
        self._exams.append(exam)
        return True

    def remove_exam(self, exam: Exam, teacher: Teacher):
        if teacher is not self._teacher:
            print('ОШИБКА! У вас нет прав доступа.')
            return False
        if exam not in self._exams:
            print('ОШИБКА! Экзамен отсутствует в списке.')
            return False
        self._exams.remove(exam)
        return True

    def change_places(self, number: int, teacher: Teacher):
        if teacher is not self._teacher:
            print('ОШИБКА! У вас нет прав доступа.')
            return False
        self._count_place = number

    def get_info(self):
        return "Факультет: {0} | Преподаватель: {1} | Количество абитуриентов: {2} | Количество экзаменов: {3} | Бюджетные места: {4}".format(
            self.get_name(), self._teacher.get_shortname(), len(self._enrollees), len(self._exams), self._count_place)

    def get_exam(self, id):
        exam = any((exam.id == id for exam in self._exams))
        return exam

    def get_exams(self, teacher: Teacher):
        if teacher is not self._teacher:
            print('ОШИБКА! У вас нет прав доступа.')
            return False
        return self._exams

    def start_exam(self, id, enrollee: Enrollee):
        if enrollee.rating.get_answer(id) is not None:
            print('ОШИБКА! Данный экзамен уже пройден.')
            return False
        if not any((exam.id == id for exam in self._exams)):
            print('ОШИБКА! Неверный ID экзамена.')
            return False
        return self.get_exam(id)
