import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or min > max or quantity < 1 or quantity > (max - min + 1):
        print('Некоректні вхідні данні')
        return []
    numbers_set = set()
    while len(numbers_set) < quantity:
        numbers_set.add(random.randint(min, max))
    winning_numbers = sorted(list(numbers_set))
    
    return winning_numbers

# Приклад використання функції:

random_numbers = get_numbers_ticket(1, 10, 5)
if random_numbers:
    print(f'Ваші лотерейні числа: {random_numbers}')