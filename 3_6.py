# 6
# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(str):
    return str.capitalize()
print(int_func(input("Введите слово: ")))

def int_func(str):
    return str.capitalize()
arr = input("Введите предложение: ").split()
i = 0
strr = ''
sep = ''
while i < len(arr):
    strr = strr + sep + int_func(arr[i])
    sep = ' '
    i += 1
print(strr)