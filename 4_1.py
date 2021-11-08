# 1
#
# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, hours, salary_per_hour, prize = argv

hours = int(hours)
salary_per_hour = float(salary_per_hour)
prize = float(prize)
total_salary = hours * salary_per_hour + prize
print(f"Зарплата сотрудника: {total_salary}")
