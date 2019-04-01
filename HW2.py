from random import randint

# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
# сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль,
# если он ввел 0 в качестве делителя.

s = ['+', '-', '*', '/']
while True:
    sym = input("Введите знак операции \'+\',\'-\',\'*\',\'/\' или же 0 для выхода: ")

    if sym == '0':
        break
    elif sym not in s:
        print("Введен неверный символ , повторите ввод:")
        continue
    try:

        a = (input("Введите первое число:"))
        b = (input("Введите второе число:"))
        float(a)
        float(b)
    except ValueError:
        print("Введены не числа повторите ввод")
        continue
    if sym == '/' and b == '0':
        print("Делитель не может быть равен 0")
        continue
    print(f'{a} {sym} {b} =', eval(f'{a}{sym}{b}'))

# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

c = 0
nc = 0
n = str(input('Введите число'))
for x in n:
    if int(x) % 2 > 0:
        nc += 1
    else:
        c += 1
print(f'В числе {n} {c} четных и {nc} нечетных цифр')

# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, то надо вывести число 6843.
n = str(input('Введите число'))
print(int(n[::-1]))

# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
n = int(input("Введите количество элементов n:"))
print(f"Сумма последовательности ранва {sum([1 / ((-2) ** x) for x in range(n)])}")

# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

for i in range(32, 128):
    print("%4d-%s" % (i, chr(i)), end='')
    if i % 10 == 0:
        print()

print()

# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем
# за 10 попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

n = 100
ans = ''
num = randint(1, n)
k = 10
while True:
    ans = int(input(f'Угадайте случайное число от 1 до {n} ,у вас {k} попыток:'))
    if ans == num:
        print("Поздравляю вы угадали!")
        break
    elif k == 1:
        print("Попытки закончились")
        break
    else:
        if ans > num:
            print("Ваше число больше.")
        else:
            print("Ваше число меньше.")

        k -= 1

# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
n = int(input("Введите последнее число последоватеьности:"))
if sum([x for x in range(1, n + 1)]) == n * (n + 1) / 2:
    print("Равенство 1+2+...+n = n(n+1)/2 выполняеться")
else:
    print("Равенство 1+2+...+n = n(n+1)/2 не выполняется")

# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых
# чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
nums = []
count = 0
while True:
    n = str(input("Введите число:"))
    nums.append(n)
    ans = input("Хотите ввести еще одно число? Y/N").lower()
    if ans == 'y':
        continue
    else:
        x = input("Какую цифру ищем?")
    for num in nums:
        for n in num:
            if n == x:
                count += 1
    print(f'{x} встречается {count} раз')
    break

# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

nums = []
max_sum = 0
summs = []
number = 0
while True:
    n = str(input("Введите число:"))
    nums.append(n)
    ans = input("Хотите ввести еще одно число? Y/N").lower()
    if ans == 'y':
        continue
    else:
        for x in nums:
            summs.append(sum([int(n) for n in x]))
    max_sum = max(summs)
    number = nums[summs.index(max_sum)]
    print(f'Наибольшая сумма цифр {max_sum} у числа {number}')
    break
