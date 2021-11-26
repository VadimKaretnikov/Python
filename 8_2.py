# 2.
#
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroDiv(Exception):

    def __str__(self) -> str:
        return "Знаменатель должен быть отличен от 0."


try:
    numerator = int(input("Введите Числитель: "))
    denominator = int(input("Введите Знаменатель: "))
    if denominator == 0:
        raise ZeroDiv
except ValueError:
    print("Вы ввели НЕ число")
except ZeroDiv as err:
    print(err)
else:
    print(f"{numerator} / {denominator} = {numerator / denominator}")
