from datetime import datetime

def get_days_from_today(date):
    try:
        # Конвертуємо введену дату у формат datetime
        specified_date = datetime.strptime(date, '%Y-%m-%d')
        # Отримуємо сьогоднішню дату
        today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
        # Рахуємо різницю між сьогоднішньою та веденою датою
        difference = today - specified_date
        # Повертаємо кількість днів
        return difference.days
    except ValueError:
        # Викликаємо виняток, якщо введений формат дати не правильний
        return 'Неправильний формат дати. Використовуйте  формат РРРР-ММ-ДД'
    
print(get_days_from_today('1995-05-25'))    
print(get_days_from_today('1995-05-25 15:20:30'))