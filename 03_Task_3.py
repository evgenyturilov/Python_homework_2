# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности

import random
list_of_numbers = list()

for i in range(0,15): list_of_numbers.append(random.randint(0,10))
print(list_of_numbers)

# Решение 1. Алгоритмическое. Функция создает список из неповторяющихся элементов исходного списка без упорядочивания

def sort(nums):                                     
    sorted_nums = []
    for num in nums:
        if num in sorted_nums:
            continue
        else:
            sorted_nums.append(num)
    return sorted_nums

print(sort(list_of_numbers))

# Решение 2 (с использованием встроенной функции python - 'set')

def set_sort(nums):
    sorted_nums = []
    unique_numbers = set(list_of_numbers)
    for num in unique_numbers: sorted_nums.append(num)
    return sorted_nums

print(set_sort(list_of_numbers))

# Решение 3 (оптимизация использования функции set)

print(list(set(list_of_numbers)))