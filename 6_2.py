# 2.
# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    _length: int
    _width: int

    def __init__(self, length: int, widht: int):
        self._length = length
        self._width = widht

    def total(self):
        self.weight = 25
        self.thickness = 5
        total = self._length * self._width * self.weight * self.thickness / 1000
        print(f"{self._length}м*{self._width}м*{self.weight}кг*{self.thickness}см = {int(total)} т")


x = Road(20, 5000)
x.total()
