# 1.
#
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class MyDate():
    def __init__(self, date_str):
        self.__date_str = date_str
        dd_mm_yyyy = date_str.split('-')
        self.__dd = dd_mm_yyyy[0]
        self.__mm = dd_mm_yyyy[1]
        self.__yy = dd_mm_yyyy[2]

    @classmethod
    def To_Number(cls, date_str):
        my_dt = cls(date_str)
        return 10000 * int(my_dt.__yy) + 100 * int(my_dt.__mm) + int(my_dt.__dd)

    @staticmethod
    def Is_Leap_Year(yy):
        if int(yy) % 4 == 0 and not int(yy) % 100 == 0:
            return True
        else:
            return False

    @staticmethod
    def Is_Date_Valid(date_str):
        dd_mm_yyyy = date_str.split('-')
        dd = dd_mm_yyyy[0]
        mm = dd_mm_yyyy[1]
        yy = dd_mm_yyyy[2]
        if len(yy) != 4:
            return False, 'Год должен содержать 4 цифры'
        if not str(yy).isdigit():
            return False, 'Год должен содержать только цифры'
        if len(mm) != 2:
            return False, 'Месяц должен содержать две цифры'
        if not str(mm).isdigit():
            return False, 'Месяц должен содержать только цифры'
        if int(mm) < 1 or int(mm) > 12:
            return False, 'Месяц должен быть от 01 до 12'
        if len(dd) != 2:
            return False, 'День должен содержать две цифры'
        if not str(dd).isdigit():
            return False, 'День должен содержать только цифры'
        mm_dd_arr = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        mm_max_day = mm_dd_arr[int(mm)]
        if int(mm) == 2 and MyDate.Is_Leap_Year(yy):
            mm_max_day = 29
        if int(dd) < 1 or int(dd) > mm_max_day:
            return False, f"День должен быть от 1 до {mm_max_day}"
        return True, 'Дата корректная'


date_str = '31-11-2004'
res, err_text = MyDate.Is_Date_Valid(date_str)
if not res:
    print(f"Ошибка в дате: {err_text}")
else:
    dt = MyDate.To_Number(date_str)
    print(f"Успешно! Преобразование в число {dt}")


