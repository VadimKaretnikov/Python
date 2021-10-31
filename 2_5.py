# 2_5
# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,то новый элемент с тем же значением должен разместиться после них.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].


my_list = [7, 5, 3, 3, 2]
rating = my_list.copy()
n = 1
while n <= 5:
    new_n = int(input("Введите рейтинг"))
    n += 1
    finished = False
    i = 0
    while i < len(rating):
        if new_n > rating[i]:
            rating.insert(i, new_n)
            finished = True
            break
        i += 1
    if not finished:
        rating.append(new_n)
    print(rating)
