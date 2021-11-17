# 5.
# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title: str

    def __init__(self, title: str):
        self.title = title

    def drow(self):
        return "Запуск отрисовки"


class Pen(Stationery):
    def drow(self):
        return "Запуск отрисовки ручкой"


class Pencil(Stationery):
    def drow(self):
        return "Запуск отрисовки карандашом"


class Handle(Stationery):
    def drow(self):
        return "Запуск отрисовки маркером"


parker = Pen("Parker")
faber_castell = Pencil("Faber-Castell")
touch = Handle("TOUCH")
print(f"{parker.title}. {parker.drow()}")
print(f"{faber_castell.title}. {faber_castell.drow()}")
print(f"{touch.title}. {touch.drow()}")
