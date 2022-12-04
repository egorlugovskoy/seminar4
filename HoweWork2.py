# B. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

with open('file1.txt', 'w') as file:
    file.write('3*x**8+9*x**7+3*x**6+3*x**5+8*x**4+3*x**3+10*x**2+2*x+4')
with open('file2.txt', 'w') as file:
    file.write('6*x**8+10*x**7+7*x**5+10*x**4+7*x**3+5*x**2+10')
with open('file1.txt','r') as file:
    p_1 = file.readline()
    N_1 = p_1.split()
with open('file2.txt','r') as file:
    p_2 = file.readline()
    N_2 = p_2.split()
print(f'{N_1} + {N_2}')
sum = N_1 + N_2
with open('filesum.txt', 'w') as file:
    file.write(f'Первый файл {N_1} + Второй файл {N_2}')
    print(f'Первый файл {N_1} + Второй файл {N_2}') ## для себя 