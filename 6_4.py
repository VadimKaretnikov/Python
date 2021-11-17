# 4.
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return "Машина поехала"

    def stop(self):
        return "Машина остановилась"

    def turn_left(self):
        return "Машина повернула налево"

    def turn_right(self):
        return "Машина повернула направо"

    def show_speed(self):
        return f"Ваша скорость {self.speed}"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f"Снизьте скорость до 60 км/ч"
        else:
            return f"Ваша скорость {self.speed}"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f"Снизьте скорость до 40 км/ч"
        else:
            return f"Ваша скорость {self.speed}"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


sport = SportCar(200, "Желтый", "Ferrari", False)
town = TownCar(70, "Голубой", "RR Evoque", False)
work = WorkCar(40, "Белый", "Porter", False)
police = PoliceCar(60, "Белый", "Ford", True)

print(f"{town.name}. {town.show_speed()}")
print(f"{police.name}: {police.stop()}")
print(f"{sport.name}: {sport.turn_left()}")
print(f"{work.name} цвет {work.color}: {work.go()}")
print(f"{town.name} едет со скоростью {town.speed} км/ч")


