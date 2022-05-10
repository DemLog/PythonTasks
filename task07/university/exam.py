import itertools


class Rating:

    def __init__(self):
        self._answers = {}
        self._rating = {}

    def get_rating(self, id: int):
        return self._rating.get(id)

    def get_answers(self, id: int):
        return self._answers.get(id)

    def set_rating(self, id: int, score: float):
        if self.get_answers(id) is None:
            print('ОШИБКА! Невозможно поставить оценку за этот экзамен, т.к. абитуриент его не проходил.')
            return False
        self._rating[id] = score
        return True

    def set_answer(self, id: int, answer: list):
        if self.get_answers(id) is not None:
            print('ОШИБКА! Абитуриент уже прошел данный экзамен.')
            return False
        self._answers[id] = answer
        return True


class Exam:
    newid = itertools.count()

    def __init__(self, name: str):
        self.id = next(Exam.newid)
        self._name = name
        self._questions = []
        print(self.id)

    def get_name(self):
        return self._name

    def __getitem__(self, item):
        return self._questions[item]

    def __delitem__(self, key):
        self._questions.pop(key)

    def get_questions(self):
        return self._questions

    def add(self, question: str):
        self._questions.append(question)
