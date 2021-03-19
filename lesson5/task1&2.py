# Задание 1. Функция-генератор rand_nums
# Написать функцию-генератор rand_nums, генерирующую N случайных целых чисел в диапазоне 1 до 100 (включительно).
# Количество чисел N, которое выдаст генератор передается в функцию через параметр:
#
# >>> rand15 = rand_nums(15)
# >>> next(rand15) # 1-й вызов
# 11
# >>> next(rand15) # 2-й вызов
# 38
# ...
# >>> next(rand15) # 15-й вызов
# 7
# >>> next(rand15) # 16-й вызов
# ...StopIteration...

# 2. * Задание 2. Выражение-генератор
# Создайте объект-генератор, выбирающий из функции-генератора rand_nums, написанного в предыдущем задании,
# только нечетные
# числа.
# Проитерируйтесь по этому объекту-генератору и выведите на экран для каждого значения на отдельной строке: порядковый
# номер (начиная с 1-го) и соответствующее ему значение. Например:
# 1 11
# ...
# 10 7
#
# Ниже в комментарии к задаче напишите какое N надо передать в функцию-генератор rand_nums, чтобы объект-генератор
# вернул нам не менее 20 значений.
# Например:
# В rand_nums надо передать ______ (число)

import random


def rand_nums(n):
    for num in range(n):
        yield random.randint(1, 101)


rand15 = enumerate(rand_nums(15))

# rand15 = enumerate((num for num in rand_nums(20) if num % 2 == 1))   # Задание 2

print(next(rand15))
print(next(rand15))
print(next(rand15))
print(next(rand15))
print(next(rand15))
print(next(rand15))
print(next(rand15))
print(next(rand15))
print(next(rand15))
print(next(rand15))
print(next(rand15))
print(next(rand15))
print(next(rand15))
print(next(rand15))
print(next(rand15))
print(next(rand15))


# def rand_nums(n):
#         for i in range(1, 101):
#             yield n
#             n = random.randint(n)
#
#
# for random_number in rand_nums(15):
#     print("And the next number is... %d!" % (random_number))
