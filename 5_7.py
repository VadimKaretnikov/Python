# 7
#
# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджер контекста.

import json

f = open("5_7.txt", "r")

fin_res = []
firms_res = {}
total_profit = 0
profit_cnt = 0
for s in f:
    arr = s.split()
    profit = float(arr[2]) - float(arr[3])
    if profit >= 0:
        total_profit = total_profit + profit
        profit_cnt += 1
    firms_res[arr[0]] = profit
fin_res.append(firms_res)
if profit_cnt > 0:
    avg_profit = total_profit / profit_cnt
else:
    avg_profit = 0
fin_res.append({'average_profit': avg_profit})
with open("5_7.json", "w") as write_f:
    json.dump(fin_res, write_f)