from random import randint

# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
d = {}
for n in range(2, 10):
    d[n] = len([i for i in range(2, 100) if i % n == 0])
print(d)

# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

m = [randint(1, 100) for i in range(10)]
n = [x for x in range(10) if m[x] % 2 == 0]
print(m)
print(n)

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint

m = [randint(1, 100) for i in range(10)]
print(m)
m[m.index(max(m))], m[m.index(min(m))] = m[m.index(min(m))], m[m.index(max(m))]
print(m)

# 4. Определить, какое число в массиве встречается чаще всего.
m = [randint(1, 5) for i in range(10)]
num_count = [m.count(m[x]) for x in range(10)]
max_num_count = m[num_count.index(max(num_count))]
print(f'Чащ всего встречаеться {max_num_count} {max(num_count)} раз.')

# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.
m = [randint(-100, 100) for i in range(10)]
min_num = min(m)
min_index = m.index(min_num)
print(f'{min_num} index {min_index}')

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
m = [randint(1, 100) for i in range(10)]
max_ind = m.index(max(m))
min_ind = m.index(min(m))
print(m)
if max_ind > min_ind:
    print(sum(m[min_ind + 1:max_ind]))
else:
    print(sum(m[max_ind + 1:min_ind]))

# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.
m = [randint(1, 100) for i in range(10)]
print(min(m))
m.remove(min(m))
print(min(m))

# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.
M = 5
N = 4
a = []
for i in range(N):
    b = []
    s = 0
    print("%d-я строка:" % i)
    for j in range(M - 1):
        n = int(input())
        s += n
        b.append(n)
    b.append(s)
    a.append(b)

for i in a:
    print(i)

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
a = []
for i in range(3):
    a.append([randint(1, 100) for n in range(3)])
for i in a:
    print(i)
max_of_min = max([min(x) for x in a])
print(f'максимальный элемент среди минимальных элементов {max_of_min}')
