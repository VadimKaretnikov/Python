# 1.
# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep
class TrafficLight:
    # 7 + 2 + 6
    try:
        i_rate = int(input("How many reps? (One cycle - 15 sec. Cycle can't be more than 30 ): ->>> "))
        if i_rate > 30:
            raise BaseException
    except BaseException:
        print("Error. Please, enter to int number.")
        exit(-1)

    __color = ('red', 'yellow', 'green')

    def running(self):
        i_cycle = 0

        while i_cycle < self.i_rate:
            i_cycle += 1
            i_text = "The traffic light is now on:"

            for i_color in TrafficLight.__color:
                if i_color == 'red':
                    print(i_text, i_color)
                    sleep(7)
                elif i_color == 'yellow':
                    print(i_text, i_color)
                    sleep(2)
                elif i_color == 'green':
                    print(i_text, i_color)
                    sleep(6)
                else:
                    print("Error. Please restart program.")
                    exit(-1)

TrafficLight().running()