# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# Решение 1

print('Введите натуральное число:')
user_number = int(input())

def find_dividers(num):                         # Функция разлагает натуральное число на множители и сохраняет результат в виде листа строк
    list_of_dividers = list()
    divider = 2                                 # Начинаем с 2 т.к. любое число делится либо на 1, либо на само себя
    count = 0
    while divider < 100:                        # Цикл проверки делимости заданного числа на первый множитель   
        if num%divider == 0:
            count += 1                          # Если множитель проходит проверку, ведем подсчет количества прохождений. Это понадобится для вывода отведа в виде степени множителя
            num = num/divider   
        else:                                   # Если множитель проверку не проходит, то увеличиваем его значение на 1 и начинаем проверку заново
            if count != 0 and count != 1:
                list_of_dividers.append(f'{divider}**{count}')
            elif count == 1:
                list_of_dividers.append(str(divider))
            divider += 1
            count = 0
    return list_of_dividers

print(f'Простые множители числа {user_number}:')
print(find_dividers(user_number))

# Решение 2 (Позволяет выбрать форму предоставления результатов работы программы)

print('Введите натуральное число:')
user_number = int(input())
print('В какой форме предоставить результат?\n  Для краткого представления введите     0\n  Для подробного представления введите   1')
user_choise = int(input())

def find_dividers(num):                         # Функция разлагает натуральное число на множители
    list_of_dividers = list()
    divider = 2
    while divider < 100:
        if num%divider == 0:
            list_of_dividers.append(divider)
            num = num/divider
        else:
            divider += 1
    return list_of_dividers

def sort_dividers(lst):                         # Функция определяет количество повторяющихся чисел в списке и выводит результат в виде данного числа в степени количества повторений
    sorted_lst = list()
    sorter = 2
    while sorter < 100:
        count = sum(True for i in lst if i == sorter)
        if count != 0 and count != 1:
            sorted_lst.append(f'{sorter}**{count}')
        elif count == 1:
            sorted_lst.append(str(sorter))
        sorter += 1
    return sorted_lst

dividers = find_dividers(user_number)
if user_choise == 1:
    print(f'Простые множители числа {user_number}:')
    print(dividers)
elif user_choise == 0:
    print(f'Простые множители числа {user_number}:')
    print(sort_dividers(dividers))
else:
    print(f'Вы ввели {user_choise}, требуется 0 или 1. Попробуйте еще раз! ')
