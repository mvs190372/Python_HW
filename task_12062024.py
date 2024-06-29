import random
import warnings
from colorama import init, Fore, Style
import sys


print("Задание 1. Проверка типов аргументов.")
# Домашнее задание на тему декораторы
# 1. Проверка типов аргументов: Напишите декоратор, который будет проверять типы аргументов
# передаваемой функции и выводить предупреждение в случае несоответствия.
# Что касается вызова предупреждений в Python, вы можете использовать модуль warnings.
# Вот пример того, как можно вызвать предупреждение:
# import warnings
# def some_function(value):
#     if value < 0:
#         warnings.warn("Значение меньше нуля", UserWarning)
#
# some_function(-5)
# https://docs.python.org/3/library/warnings.html


# warnings.filterwarnings("ignore")


def check_args_types(func: object) -> object:
    def wrapper(*args) -> bool:
        correct = True
        for arg in args:
            if type(arg) is not int:
                correct = False
                break
            else:
                continue
        if correct:
            func(*args)
        else:
            # print(f"Функция {func.__name__}, аргументы - {args}: некорректный тип данных в аргументах.")
            warnings.warn(f"Функция {func.__name__} вызвана с аргументами {args}. Некорректные аргументы, все аргументы должны быть типа int.", UserWarning, stacklevel=2)

        return correct

    return wrapper


def print_nums(*args):
    string = ""
    for arg in args:
        if string != "":
            string += " "
        string += str(arg)
    print(string)


def custom_warn(message, category, filename, lineno, file=None, line=None):
    sys.stdout.write(warnings.formatwarning(message, category, filename, lineno))


warnings.showwarning = custom_warn


check_args_types(print_nums)(-5, 6, 7, 8, 9)
check_args_types(print_nums)(10, 20, 30, "uykwegrfyuewgw")
check_args_types(print_nums)(1, 2, 3, 4)
check_args_types(print_nums)(1, -2.5, 3, "klkjhlkllililk")
check_args_types(print_nums)(-1, -2, -3, "dsdkhjdsfkljhjh")


print("*************************************************")
print("Задание 2. Изменение цвета вывода в консоли.")
# 2. Декоратор для изменения цвета вывода в консоли: Напишите декоратор, который будет
# изменять цвет текста, выводимого функцией в консоли.
# В Python вы можете изменить цвет вывода текста в консоли, используя модуль colorama.
# Вот пример того, как это можно сделать:
# from colorama import init, Fore, Back, Style
# init()  # Инициализация colorama
# def print_colorful(text, color=Fore.WHITE):
#     print(color + text + Style.RESET_ALL)
#
# print_colorful("Этот текст будет выводиться белым", Fore.WHITE)
# print_colorful("А этот текст будет выводиться красным", Fore.RED)

init()


def change_color(func):
    def wrapper(text):
        match(random.randint(1, 16)):
            case 1:
                color = Fore.RED
            case 2:
                color = Fore.WHITE
            case 3:
                color = Fore.BLUE
            case 4:
                color = Fore.CYAN
            case 5:
                color = Fore.GREEN
            case 6:
                color = Fore.BLACK
            case 7:
                color = Fore.LIGHTBLACK_EX
            case 8:
                color = Fore.LIGHTBLUE_EX
            case 9:
                color = Fore.LIGHTGREEN_EX
            case 10:
                color = Fore.YELLOW
            case 11:
                color = Fore.LIGHTCYAN_EX
            case 12:
                color = Fore.LIGHTMAGENTA_EX
            case 13:
                color = Fore.LIGHTRED_EX
            case 14:
                color = Fore.LIGHTWHITE_EX
            case 15:
                color = Fore.LIGHTYELLOW_EX
            case _:
                color = Fore.MAGENTA
        func(color + text + Style.RESET_ALL)

    return wrapper


inputted_text = input("Введите текст: ")
print(inputted_text)
print("*******************")
change_color(print)(inputted_text)
change_color(print)(inputted_text)
change_color(print)(inputted_text)
change_color(print)(inputted_text)
change_color(print)(inputted_text)
change_color(print)(inputted_text)
change_color(print)(inputted_text)
change_color(print)(inputted_text)
change_color(print)(inputted_text)
change_color(print)(inputted_text)
change_color(print)(inputted_text)
change_color(print)(inputted_text)
change_color(print)(inputted_text)
change_color(print)(inputted_text)
change_color(print)(inputted_text)
change_color(print)(inputted_text)


# import datetime
#
#
# def logger(func):
#     def wrapper(*args, **kwargs):
#         with open('log.txt', 'a', encoding='utf-8') as f:
#             dt_now = datetime.datetime.now()
#             data = f"\n{dt_now} ТРАССИРОВКА: вызвана {func.__name__}() " f"с аргументами: {args} {kwargs}"
#             original_result = func(*args, **kwargs)
#             data += f", вернула: {original_result!r}"
#             f.write(data)
#             f.close()
#
#         return original_result
#
#     return wrapper
#
#
# def hello(name: str, volume: float = 0.2) -> str:
#     return f"Hello, {name}! volume = {volume}!"
#
#
# print(logger(hello)("John", volume=0.6))
# print(logger(hello)("Alice", volume=0.3))
# print(logger(hello)("Mary", volume=0.8))
#
# print("*******************************")
#
#
# def check_positive(func):
#     def wrapper(*args) -> bool:
#         original_result = True
#         for arg in args:
#             if float(arg) <= 0:
#                 original_result = False
#                 break
#             else:
#                 continue
#
#         return original_result
#
#     return wrapper
#
#
# @check_positive
# def print_nums(*args):
#     string = ""
#     for arg in args:
#         string += str(arg) + " "
#     print(string)
#
#
# print(print_nums(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(print_nums(1, 2, 3, -4, 5, 6, 7, 8, 9))


# nums_list = [2, -1, 5, -7, 8, -10, 8, 2]
# print(sorted(nums_list, key=lambda x: x < 0))

# Цифровой корень — это рекурсивная сумма всех цифр числа.
# Учитывая n, возьмите сумму цифр n. Если это значение имеет более одной цифры,
# родолжайте уменьшать таким образом, пока не получите однозначное число.
# ходные данные будут неотрицательным целым числом.
# 16  -->  1 + 6 = 7
# 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2


# def digit_root(number: int) -> int:
#     if len(str(number)) == 1:
#         return number
#     summa = 0
#     for char in str(number):
#         summa += int(char)
#     return digit_root(summa)


# print(digit_root(12345))

# Есть словарь, нужно рекурсивно пройтись по всем вложенным элементами и изменить значение
# ключа на то же значение, только в нижнем регистре.

# shoping_cart = {
#     'ПрОдукты': {
#         'фрукты': {
#             'яБлоки': 50,
#             'банаНы': 30
#         },
#         'овощИ': {
#             'морКовь': 20,
#             'огурцы': 15
#         }
#     },
#     'одеЖда': {
#         'мужская': {
#             'руБАШка': 70,
#             'брюки': 80
#         },
#         'женская': {
#             'платьЕ': 100,
#             'юбка': 60
#         }
#     }
# }
#
#
# def dict_keys_to_lowercase(dictionary: dict) -> dict:
#     lowercase_dictionary = {}
#     for key, value in dictionary.items():
#         if isinstance(value, dict):
#             lowercase_dictionary[key.lower()] = dict_keys_to_lowercase(value)
#         else:
#             lowercase_dictionary[key.lower()] = value
#     return lowercase_dictionary
#
#
# print(dict_keys_to_lowercase(shoping_cart))
