# 6
#
# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
#
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

f = open("5_6.txt", "r")

studies = {}

for s in f:
    arr = s.split()
    study = arr[0].replace(':', '')
    i = 1
    amnt = 0
    while i < len(arr):
        str = arr[i]
        amnt_str = ''
        j = 0
        while j < len(str):
            if str[j].isdigit():
                amnt_str = amnt_str + str[j]
            j += 1
        amnt = amnt + int(amnt_str)

        i += 1
    studies[study] = amnt
print(studies)

f.close()