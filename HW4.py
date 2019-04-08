from random import randint
import cProfile
import  timeit
import time
# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания
# первых трех уроков.
#  Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# В одномерном массиве целых чисел определить два наименьших элемента.
# m = [randint(1, 100) for i in range(1000)]
m=[randint(1,100) for i in range(1000)]
def min_num(x):
    min_1=min(x)
    x.remove(min(x))
    min_2=min(x)
    return min_1, min_2


def min_num2(x):
    min_1 = x[0]
    min_2 = x[0]
    for i in x:
        if min_1 >= i:
            min_1 = i
        if min_2 >= i and i>min_1:
            min_2 = i
    return min_1, min_2

print(timeit.timeit('min_num2(m)',setup="from __main__ import min_num2 , m",number=100))
print(timeit.timeit('min_num(m)',setup="from __main__ import min_num , m",number=100))
# # # 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# # # Без использования «Решета Эратосфена»;
# # # Используя алгоритм «Решето Эратосфена»
# # # Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.
