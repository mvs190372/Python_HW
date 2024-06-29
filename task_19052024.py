import sys


# Задание 1


def sum_digits(n):
    return sum(map(int, str(n)))


print("Задание 1. Пользователь вводит с клавиатуры два числа.")
print("Нужно посчитать отдельно сумму четных, нечетных и чисел, кратных 9")
print("в указанном диапазоне, а также среднеарифметическое каждой группы.")
print("***********************")
try:
    number1 = int(input("Введите начало диапазона целых чисел: "))
except ValueError:
    print("Ошибка ввода. Программа завершена.")
    sys.exit(-1)
try:
    number2 = int(input("Введите конец диапазона целых чисел: "))
except ValueError:
    print("Ошибка ввода. Программа завершена.")
    sys.exit(-2)
if number1 > number2:
    number1, number2 = number2, number1
sum_even = 0
count_even = 0
sum_odd = 0
count_odd = 0
sum_9 = 0
count_9 = 0
for i in range(number1, number2 + 1, 1):
    if i % 2 == 0:
        sum_even += i
        count_even += 1
    else:
        sum_odd += i
        count_odd += 1
    if sum_digits(abs(i)) % 9 == 0:
        sum_9 += i
        count_9 += 1
else:
    print(f"Диапазон: от {number1} до {number2}")
    print(f"Сумма четных чисел диапазона = {sum_even}")
    print(f"Сумма нечетных чисел диапазона = {sum_odd}")
    print(f"Сумма чисел, кратных 9 = {sum_9}")
    try:
        avg_even = float(sum_even / count_even)
    except ZeroDivisionError:
        print("Сднеарифметическое группы чётных чисел невозможно вычислить, т.к. указанная группа пуста.")
    else:
        print(f"Среднеарифметическое четных чисел = {avg_even}")
    try:
        avg_odd = float(sum_odd / count_odd)
    except ZeroDivisionError:
        print("Сднеарифметическое группы нечётных чисел невозможно вычислить, т.к. указанная группа пуста.")
    else:
        print(f"Среднеарифметическое нечетных чисел = {avg_odd}")
    try:
        avg_9 = float(sum_9 / count_9)
    except ZeroDivisionError:
        print("Сднеарифметическое группы чисел, кратных 9, невозможно вычислить, т.к. указанная группа пуста.")
    else:
        print(f"Среднеарифметическое чисел, кратных 9 = {avg_9}")

# Задание 2
print("\nЗадание 2. Пользователь вводит любое целое число.")
print("Необходимо из этого целого числа удалить все цифры 3 и 6 и вывести обратно на экран.")
print("Будет плюсом если вы используете управляющие операторы continue, break и else.")
print("***********************")
try:
    number = int(input("Введите целое число: "))
except ValueError:
    print("Ошибка ввода. Программа завершена.")
    sys.exit(-3)

# Способ 1
number1 = str(number).replace("3", "").replace("6", "")
if number1 == "" or number1 == "-":
    print(f"После удаления из числа {number} цифр 3 и 6 число \"исчезло\".")
else:
    print(f"После удаления из числа {number} цифр 3 и 6 получилось число {number1}.")

# Способ 2 - с использованием break
# temp = str(number)
# i = 0
# number1 = ""
# while True:
#     if i >= len(temp):
#         break
#     if temp[i] != "3" and temp[i] != "6":
#         number1 += temp[i]
#     i += 1
# if number1 == "" or number1 == "-":
#     print(f"После удаления из числа {number} цифр 3 и 6 число \"исчезло\".")
# else:
#     print(f"После удаления из числа {number} цифр 3 и 6 получилось число {number1}.")

# Способ 3 - с использованием continue и else
# temp = str(number)
# i = 0
# number1 = ""
# while i < len(temp):
#     if temp[i] == "3" or temp[i] == "6":
#         i += 1
#         continue
#     number1 += temp[i]
#     i += 1
# else:
#     if number1 == "" or number1 == "-":
#         print(f"После удаления из числа {number} цифр 3 и 6 число \"исчезло\".")
#     else:
#         print(f"После удаления из числа {number} цифр 3 и 6 получилось число {number1}.")
