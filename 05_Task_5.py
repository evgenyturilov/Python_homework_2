# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def coeffs_of_polynome(polynome):                   # Функция, которая находит коэффициенты многочлена в целочисленном формате
    coeff_3 = int(polynome.split()[-1])
    if polynome.split()[-2] == '-':
        coeff_3 *= -1
    space_split = polynome.split()
    coeff_2 = int(space_split[2].split('X')[0])
    if space_split[1] == '-':
        coeff_2 *= -1
    coeff_1 = int(polynome.split('X')[0])
    return coeff_1, coeff_2, coeff_3

with open(r'D:\GB_Developer\1.6 Знакомство с Python\Python\Py_Homework\Python_homework_2\05_Task_5_file_1.txt', 'r') as file_1:
    polynome_1 = file_1.read()
with open(r'D:\GB_Developer\1.6 Знакомство с Python\Python\Py_Homework\Python_homework_2\05_Task_5_file_2.txt', 'r') as file_2:
    polynome_2 = file_2.read()

coeffs_1 = coeffs_of_polynome(polynome_1)
coeffs_2 = coeffs_of_polynome(polynome_2)
coeffs_3 = list()
for i in range(0,3):
    coeffs_3.append(coeffs_1[i] + coeffs_2[i])

#print(coeffs_1)
#print(coeffs_2)
#print(coeffs_3)
#print(f'{coeffs_3[0]}X**2 + {coeffs_3[1]}X = {coeffs_3[2]}')

with open(r'D:\GB_Developer\1.6 Знакомство с Python\Python\Py_Homework\Python_homework_2\05_Task_5_file_3.txt', 'w') as file_3:
    file_3.write(f'{coeffs_3[0]}X**2 + {coeffs_3[1]}X = {coeffs_3[2]}')