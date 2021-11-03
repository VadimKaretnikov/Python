# 3
# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(var1, var2, var3):

    if var1 > var2:
        summa = var1
        if var3 > var2:
            summa = summa + var3
        else:
            summa = summa + var2
    else:
        summa = var2
        if var3 > var1:
            summa = summa + var3
        else:
            summa = summa + var1
    return summa

print(my_func(int(input("Первый параметр: ")), int(input("Второй параметр: ")), int(input("Третий параметр: "))))