#------------------------------------------------------------------------------
# Генерувати набір унікальних випадкових сортованих чисел від 1 до 1000
# min >= 1, max <= 1000, min <= quantity <= max
#------------------------------------------------------------------------------
# трохи незрозуміла умова min <= quantity <= max - чому кількість варіантів
# не може бути менше min?
# взагалі кількість унікальних варіантів може бути менше або дорівнює
# max - min + 1

def get_numbers_ticket(min, max, quantity):
    try:
        if int(min) != min or int(max) != max or int(quantity) != quantity or min < 1 or max > 1000 or quantity > max - min + 1:
            return []
    except ValueError:
        return []
    nums = []
    for i in range(max - min + 1):
        nums.append(i + min)
    import random
    lot = random.sample(nums, quantity)
    lot.sort()
    return lot

print(get_numbers_ticket(5, 8, 3))