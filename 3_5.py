# 5
# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


sep = '%'
finished = False
def input_arr(summ):
    global finished
    str = input("Введите массив чисел: ")
    arr = str.split()
    i = 0
    while i < len(arr):
        if arr[i] == sep:
            finished = True
            return summ
        else:
            summ = summ + float(arr[i])
        i += 1
    finished = False
    return summ
summ = 0
while not finished:
    summ = input_arr(summ)
    print(f"сумма: {summ}")
