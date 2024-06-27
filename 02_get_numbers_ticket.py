#------------------------------------------------------------------------------
# Генерувати набір унікальних випадкових сортованих чисел від 1 до 1000
# min >= 1, max <= 1000, min <= quantity <= max
#------------------------------------------------------------------------------

def get_numbers_ticket(min, max, quantity):
    try:
        if type(min) != int or type(max) != int or type(quantity) != int or min < 1 or max > 1000 or quantity > max - min + 1:
            return []
    except ValueError:
        return []
    import random
    lot = random.sample(range(min, max + 1), quantity)
    lot.sort()
    return lot

print(get_numbers_ticket(5, 8, 3))