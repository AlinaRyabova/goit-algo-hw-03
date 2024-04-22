from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    # Отримуємо поточну дату
    today = datetime.today().date()
    # Створюємо список для зберігання дат привітань
    upcoming_birthdays = []

    # Проходимося по кожному користувачу у списку
    for user in users:
        # Конвертуємо день народження з рядка в об'єкт datetime
        birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()

        # Визначаємо день народження в цьому або наступному році
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Визначаємо різницю між днем народження та поточно датою
        days_until_birthday = (birthday_this_year - today).days    

        # Перевіряємо, чи день народження випадає на вихідний, переносимо на понеділок
        if 0 <= days_until_birthday <= 7:
            # Якщо день народження випадає на вихідний, переносимо в понеділок
            if birthday_this_year.weekday() >= 5:
                days_until_birthday += 7 - birthday_this_year.weekday()

            # Додаємо користувача та дату привітання до списку
            greeting_date = today + timedelta(days=days_until_birthday)
            upcoming_birthdays.append({'name': user['name'], 'greeting_date': greeting_date.strftime('%Y.%m.%d')})

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.04.23"},
    {"name": "Jane Smith", "birthday": "1990.04.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)