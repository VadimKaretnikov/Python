# 5
#
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import random

f = open("5_5.txt", "w")


s = ''
for i in range(1, 11):
  s = s + ' ' + str(random() * 100)
f.write(s)
f.close()

f = open("5_5.txt", "r")
summa = 0
for s in f:
    print(s)
    arr = s.split()
    n = 0
    while n < len(arr):
        summa = summa + float(arr[n])
        n += 1

print(f"Сумма = {summa}")
f.close()
