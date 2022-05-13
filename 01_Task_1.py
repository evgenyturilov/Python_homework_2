# Вычислить число Пи c заданной точностью d

from cmath import pi

print('Введите необходимую точность расчета:')
d = int(input())

print(round(pi,d))