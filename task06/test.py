from polynomial import Polynomial

if __name__ == '__main__':
    a = Polynomial(1, 2, 3, 4, 5)
    b = Polynomial(6, 7, 8)
    print("A: {0}".format(a))
    print("B: {0}".format(b))
    print("Сложение A + B: {0}".format(a + b))
    print("Вычитание A - B: {0}".format(a - b))
    print("Умножение A * B: {0}".format(a * b))
    print("Значение многочлена A от x=2: {0}".format(a.calculate(2)))
