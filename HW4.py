from random import randint
import cProfile
import timeit
import time

# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания
# первых трех уроков.
#  Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# В одномерном массиве целых чисел определить два наименьших элемента.
m = [randint(1, 100) for i in range(1000)]



def min_num(x):
    min_1 = min(x)
    x.remove(min(x))
    min_2 = min(x)
    return min_1, min_2


def min_num2(x):
    min_1 = x[0]
    min_2 = x[0]
    for i in x:
        if min_1 >= i:
            min_1 = i
        if min_2 >= i and i > min_1:
            min_2 = i
    return min_1, min_2


print(timeit.timeit('min_num2(m)', setup="from __main__ import min_num2 , m", number=100))
print(timeit.timeit('min_num(m)', setup="from __main__ import min_num , m", number=100))


# # # 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# # # Без использования «Решета Эратосфена»;
# # # Используя алгоритм «Решето Эратосфена»
# # # Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.
def simple():
    n = 10
    lst = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)


def simple_2():
    n = 10  # число, до которого хотим найти простые числа
    numbers = list(range(2, n + 1))
    for number in numbers:
        if number != 0:
            for candidate in range(2 * number, n + 1, number):
                numbers[candidate - 2] = 0
    print(*list(filter(lambda x: x != 0, numbers)))
print(timeit.timeit("simple", setup='from __main__ import simple', number=100))
print(timeit.timeit("simple_2", setup='from __main__ import simple_2', number=100))