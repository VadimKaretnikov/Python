def user_info_f(firstname, lastname, birth_year, city, email, phone):

    print(f"{firstname} {lastname}, год рождения {birth_year}, город {city}, email: {email}, телефон: {phone}")

    return

firstname = input("Имя: ")
lastname = input("Фамилия: ")
birth_year = int(input("Год рождения: "))
city = input("Город: ")
email = input("Email: ")
phone = input("Телефон: ")

user_info_f(firstname=firstname, lastname=lastname, birth_year=birth_year,
            city=city, email=email, phone=phone)
