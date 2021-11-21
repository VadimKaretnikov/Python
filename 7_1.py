# 1.
#
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: см. в методичке.
#
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

from copy import deepcopy

class Matrix(object):
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        return '\n'.join('\t'.join(map(str,row)) for row in self.matrix)

    def __add__(self, other):
        if self.size() == other.size():
            r_n, c_n = self.size()
            m = deepcopy(self.matrix)
            row = 0
            while row < r_n:
                col = 0
                while col < c_n:
                    m[row][col] = self.matrix[row][col] + other.matrix[row][col]
                    col += 1
                row += 1
            return Matrix(m)

    def size(self):
        return len(self.matrix), len(self.matrix[0])

m1 = Matrix([[0,1,5], [0,2,2]])
m2 = Matrix([[1,0,0], [1,1,6]])
m3 = m1 + m2
print(m1)
print(m2)
print(m3)
