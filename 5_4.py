# 4
#
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4

# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

f = open("5_4.txt", "r")
r = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре',
     'Five': 'Пять', 'Six': 'Шесть', 'Seven': 'Семь',
     'Eight': 'Восемь', 'Nine': 'Девять', 'Zero': 'Ноль'}

def translate(str):
    for i in r.keys():
        str = str.replace(i, r[i])
    return str

for s in f:
    translated = translate(s)
    print(translated)

f.close()