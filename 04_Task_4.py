# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

print('Введите значение степени многочлена:')
user_coeff = int(input())
print(f'Многочлен степени k = {user_coeff}:')

def polynome(coeff):                                           # Функция составляет многочлен степени k со случайными целочисленными коэффициентами от 0 до 100
    polynome = str()
    for i in range(coeff, 1, -1):
        variable_coeff = random.randint(0,100)
        if variable_coeff != 0:
            polynome = polynome + f'{variable_coeff}X**{i} + '

    if coeff == 0:
        polynome = '0 '
    else:
        variable_coeff_2 = random.randint(0,100)
        if variable_coeff_2 != 0:
            polynome = polynome + f'{variable_coeff_2}X + '

        variable_coeff_3 = random.randint(0,100)
        if variable_coeff_3 != 0:
            polynome = polynome + str(variable_coeff_3) + ' '
        elif variable_coeff_3 == 0:
            polynome = polynome[:-2]
    
    polynome += '= 0'
    return polynome

result = polynome(user_coeff)
print(result)
with open(r'D:\GB_Developer\1.6 Знакомство с Python\Python\Py_Homework\Python_homework_2\04_Task_4_file.txt', 'w') as file:
    file.write(result)