#Задание 1
import sys
try:
    number1=float(input("Введите число 1: "))
except ValueError:
    print("Ошибка ввода числа 1. Программа завершена.");
    sys.exit(-1)
try:
    number2=float(input("Введите число 2: "))
except ValueError:
    print("Ошибка ввода числа 2. Программа завершена.");
    sys.exit(-2)
try:
    number3=float(input("Введите число 3: "))
except ValueError:
    print("Ошибка ввода числа 3. Программа завершена.");
    sys.exit(-3)
choice=input("Введите код операции: + сложение, * умножение: ")
if choice.strip()=="+":
    print(f"{number1} + {number2} + {number3} = {number1 + number2 + number3}")
elif choice.strip()=="*":
    print(f"{number1} * {number2} * {number3} = {number1 * number2 * number3}")
else:
    print("Код операции введен неверно.")

#Задание 2
try:
    number1=float(input("\nВведите число 1: "))
except ValueError:
    print("Ошибка ввода числа 1. Программа завершена.");
    sys.exit(-4)
try:
    number2=float(input("Введите число 2: "))
except ValueError:
    print("Ошибка ввода числа 2. Программа завершена.");
    sys.exit(-5)
try:
    number3=float(input("Введите число 3: "))
except ValueError:
    print("Ошибка ввода числа 3. Программа завершена.");
    sys.exit(-6)
choice=input("Введите код операции: 1 - найти max, 2 - найти min, 3 - найти среднеарифметическое: ")
if choice.strip()=="1":
    print(f"max из чисел {number1}, {number2} и {number3} = {number1 if number1 >= number2 and number1 >= number3 else number2 if number2 >= number1 and number2 >= number3 else number3}")
elif choice.strip()=="2":
    print(f"min из чисел {number1}, {number2} и {number3} = {number1 if number1 <= number2 and number1 <= number3 else number2 if number2 <= number1 and number2 <= number3 else number3}")
elif choice.strip()=="3":
    print(f"Среднеарифметическое чисел {number1}, {number2} и {number3} = {(number1 + number2 + number3)/3}")
else:
    print("Код операции введен неверно.")

#Задание 3
try:
    number=float(input("\nВведите количество метров: "))
except ValueError:
    print("Ошибка ввода количества метров. Программа завершена.");
    sys.exit(-7)
CONST_miles_meter=0.000621
CONST_inches_meter=39.37
CONST_yards_meter=1.0936
choice=input("Введите код операции для перевода: 1 - в мили, 2 - в дюймы, 3 - в ярды: ")
if choice.strip()=="1":
    print(f"{number} в метрах = {number * CONST_miles_meter} в милях")
elif choice.strip()=="2":
    print(f"{number} в метрах = {number * CONST_inches_meter} в дюймах")
elif choice.strip()=="3":
    print(f"{number} в метрах = {number * CONST_yards_meter} в ярдах")
else:
    print("Код операции введен неверно.")    


"""
#Задание 1
print("Nothing\nwill work\nunless you do.\n")

#Задание 2
print("\"Anyone who\n\tstops\n\t\tlearning is old,\n\t\t\twhether at twenty or eighty\".\n\t\t\t\t\t\t\t\tHenry Ford\n")

#Задание 3
import sys

try:
    number1=float(input("Введите число 1: "))
except ValueError:
    print("Ошибка ввода числа 1. Программа завершена.");
    sys.exit(-1)
try:
    number2=float(input("Введите число 2: "))
except ValueError:
    print("Ошибка ввода числа 2. Программа завершена.");
    sys.exit(-2)
print(f"{number1} + {number2} = {number1 + number2}")
print(f"{number1} - {number2} = {number1 - number2}")
print(f"{number1} * {number2} = {number1 * number2}")

#Задание 4
try:
    number=float(input("\nВведите число: "))
except ValueError:
    print("Ошибка ввода числа. Программа завершена.");
    sys.exit(-3)
try:
    percent=float(input("Введите %: "))
except ValueError:
    print("Ошибка ввода %. Программа завершена.");
    sys.exit(-4)
print(f"{percent}% от числа {number} составляет {number*percent/100}")

#Задание 5
try:
    a=float(input("\nВведите сторону прямоугольника 1: "))
except ValueError:
    print("Ошибка ввода данных. Программа завершена.");
    sys.exit(-5)
try:
    b=float(input("Введите сторону прямоугольника 2: "))
except ValueError:
    print("Ошибка ввода данных. Программа завершена.");
    sys.exit(-6)
print(f"Площадь прямоугольника со сторонами {a} и {b} равна {a * b}.")
"""