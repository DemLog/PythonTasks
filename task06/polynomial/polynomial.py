class Polynomial:

    def __init__(self, *coefficients):
        self._degree = len(coefficients)
        self._coefficients = list(coefficients)

    def __getitem__(self, item):
        return self._coefficients[item]

    def __setitem__(self, key, value):
        self._coefficients[key] = value

    def __add__(self, other):
        count = max(self._degree, other._degree)
        result = [0] * count
        for i in range(0, count):
            a = 0
            b = 0
            if i < self._degree:
                a = self[i]
            if i < other._degree:
                b = other[i]
            result[i] = a + b
        return Polynomial(*result)

    def __sub__(self, other):
        count = max(self._degree, other._degree)
        result = [0] * count
        for i in range(0, count):
            a = 0
            b = 0
            if i < self._degree:
                a = self[i]
            if i < other._degree:
                b = other[i]
            result[i] = a - b
        return Polynomial(*result)

    def __mul__(self, other):
        count = self._degree + other._degree - 1
        result = [0] * count
        for i in range(0, self._degree):
            for j in range(0, other._degree):
                result[i + j] += self[i] * other[j]
        return Polynomial(*result)

    def __str__(self):
        result = ""
        for i in range(self._degree - 1, 0, -1):
            result += "{0}x^{1} + ".format(self[i], i)
        result += str(self[0])
        return result

    def calculate(self, x):
        n = self._degree - 1
        result = self._coefficients[n]
        for i in range(n - 1, -1, -1):
            result = x * result + self[i]
        return result
