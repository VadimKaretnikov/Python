# 2_3_2
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через dict

months = {1: "зима", 2: "зима", 3: "весна", 4: "весна", 5: "весна",
          6: "лето", 7: "лето", 8: "лето", 9: "осень", 10: "осень",
          11: "осень", 12: "зима"}
c = int(input("Введите месяц"))
if c <= 0 or c > 12:
    print("неверный номер месяца")
else:
    print(months[c])
