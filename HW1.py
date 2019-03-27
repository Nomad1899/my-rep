import random
import string

# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

summ = 0
mult = 1
try:
    num = int(input("Введите трехзначное число:"))
    if len(str(num)) == 3:
        for i in str(num):
            summ += int(i)
            mult *= int(i)
    else:
        print("В числе не три знака!")
except ValueError:
    print("Введено не число!")
print(summ)
print(mult)


# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5
# побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.
print(f'И= {5 & 6}')
print(f'ИЛИ={5 | 6}')
print(f'Исключительное или{5 ^ 6}')
print(f"Сдвиг влево {5 << 2}")
print(f"Сдвиг вправо {5 >> 2}")


# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
print("Координаты точки A(x1;y1):")
x1 = float(input("\tx1 = "))
y1 = float(input("\ty1 = "))

print("Координаты точки B(x2;y2):")
x2 = float(input("\tx2 = "))
y2 = float(input("\ty2 = "))

print("Уравнение прямой, проходящей через эти точки:")
k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
print(f" y = {k}x + {b}")


# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
print("Введите диапазон для случайного целого числа:")
start = int(input("\tНачало:"))
end = int(input('\tКонец:'))
print(random.randint(start, end))
print("Введите диапазон для случайного вещественного числа:")
start = float(input("\tНачало:"))
end = float(input('\tКонец:'))
print(random.uniform(start, end))
print("Введите диапазон сучайных символов:")
start = string.ascii_letters.index(input("\tНачало:"))
end = string.ascii_letters.index(input('\tКонец:')) + 1
print(''.join(random.choice(string.ascii_letters[start:end])))

# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
print("Введите диапазон для букв:")
start = string.ascii_uppercase.index(input("\tНачало:").upper()) + 1
end = string.ascii_uppercase.index(input('\tКонец:').upper()) + 1
print(f"Первая буква имеет №{start},втоая буква №{end}, между ними {abs(end - start) - 1} букв")


# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
print(string.ascii_uppercase[int(input("Введите номер буквы:")) - 1])


# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним,
# равнобедренным или равносторонним.
a = int(input("Введите длинну стороны а: "))
b = int(input("Введите длинну стороны b: "))
c = int(input("Введите длинну стороны c: "))
if (a + b) > c and (a + c) > b and (b + c) > a:
    if a == b == c:
        print("Равносторонний треугольник")
    elif a == b or b == c or a == c:
        print("Равнобедренный треугольник")
    else:
        print("Разносторонний теугольник")
else:
    print("Треугольника с заданными сторонами не существует")

#8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
year = int(input("Введите год:"))
if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print("Этот год невисокосный")
else:
    print("Это високосный год")

#9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
a=int(input("Введите первое число:"))
b=int(input("Введите второе число:"))
c=int(input("Введите третье число:"))
m=[a,b,c]
m.remove(max(m))
m.remove(min(m))
print(f"Среднее число {m[0]}")
