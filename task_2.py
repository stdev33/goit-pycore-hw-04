import random


def get_numbers_ticket(min_val, max_val, quantity):
    if min_val < 1 or max_val > 1000 or quantity < 1 or quantity > (max_val - min_val + 1):
        return []

    numbers = random.sample(range(min_val, max_val + 1), quantity)
    numbers.sort()

    return numbers


print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(1, 36, 5))
print(get_numbers_ticket(10, 20, 15))
print(get_numbers_ticket(1, 49, 50))
print(get_numbers_ticket(0, 49, 5))
print(get_numbers_ticket(1, 1001, 5))
