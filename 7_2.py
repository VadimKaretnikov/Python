# 2.
#
# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def calc_cloth(self, amnt):
        pass

    @property
    @abstractmethod
    def size(self):
        pass


class Suit(Clothes):
    def __init__(self, size):
        self.__size = size

    def __str__(self):
        print(f"Костюм роста {self.__size}")

    @property
    def size(self):
        return self.__size

    def calc_cloth(self, amnt):
        return (2 * self.__size + 0.3) * amnt


class Coat(Clothes):
    def __init__(self, size):
        self.__size = size

    def __str__(self):
        print(f"Пальто размера {self.__size}")

    @property
    def size(self):
        return self.__size

    def calc_cloth(self, amnt):
        return (self.__size / 6.5 + 0.5) * amnt


Suit1 = Suit(12)
Coat1 = Coat(14)
Cloth_amount = Suit1.calc_cloth(1) + Coat1.calc_cloth(2)
print(
    f"На один костюм размера {Suit1.size} и два пальто размера {Coat1.size} понадобится {Cloth_amount} погонных метров ткани")
