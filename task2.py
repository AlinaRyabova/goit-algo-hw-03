import random

def get_numbers_ticket(minimum: int, maximum: int, quantity: int) -> int:
    # Перевірка чи параметри відповідають обмеженням
    if minimum < 1 or maximum > 1000 or quantity < 1 or quantity > (maximum - minimum + 1):
        return []
    # Створення пустого списку для зберігання чисел
    numbers = []
    # Генерування унікальних чисел
    while len(numbers) < quantity:
        number = random.randint(minimum, maximum)
        if number not in numbers:
            numbers.append(number)
    # Повернення результату і сортування чисел
    return sorted(numbers)

lottery_numbers = get_numbers_ticket(1, 47, 4)
print("Ваші лотерейні числа:", lottery_numbers)

