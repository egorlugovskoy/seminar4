# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

import random

def stepen(k):
    for i in range(k+1):
        x = random.randint(0, 100)
        if k > 1:
            if x > 1:
                print(f'{x}x^{k} +', end=' ')
            elif x == 1:
                print(f'x^{k} +', end=' ')
        elif k == 1:
            if x > 1:
                print(f'{x}x +', end=' ')
            elif x == 1:
                print(f'x +', end=' ')
        elif k == 0:
            if x != 0:
                print(f'{x} = 0')
            else:
                print('= 0')
        x += 1
        k -= 1

k = int(input('Введите степень K: '))
stepen(k)