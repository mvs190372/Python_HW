# ПРОДВИНУТАЯ РАБОТА С ФУНКЦИЯМИ
# ==========  4  ==========
# Написать параметризуемый декоратор с именем repeat, который выполняет декорируемую функцию заданное
# количество раз.
# Это достаточно распространённая задача в сфере тестирования.
# Функция параметризации декораторов repeat принимает необязательным аргументом количество вызовов
# декорируемой функции.
# Количество вызовов декорируемой функции должно быть позиционно-ключевым аргументом, передаётся в виде
# объекта int, значение по умолчанию 2.
# Декоратор может применяться к функциям с различным набором позиционных и ключевых аргументов.
# Написанный декоратор необходимо протестировать вручную с помощью дополнительной произвольной функции.
# Пример ручного теста:
#     >>> def testing_function():
#     ...     print('python')
#     ...
#     >>> testing_function = repeat(testing_function)(4)
#     >>>
#     >>>
#     >>> testing_function()
#     python
#     python
#     python
#     python


def testing_function() -> None:
    """Функция для тестирования декоратора logger, печатает слово <<python>>."""
    print('python')


def repeat(func, *args, **kwargs) -> None:
    """Функция-декоратор для нагрузочного тестирования, принимает на вход количество повторений.
       По умолчанию повторений 2."""
    def wrapper(count=2):
        for i in range(count):
            func(*args, **kwargs)

    return wrapper


def testing_function_1(a: float, b: float) -> float:
    """Функция для тестирования декоратора logger, вычисляет сумму операндов a и b и печатает результат."""
    print(f"{a} + {b} = {a+b}")


def testing_function_2(x: float, y: float, z: float, operation="+"):
    """Функция для тестирования декоратора logger, операция задается параметром operation,
        вычисляет результат заданной операции над операндами a,b и c и печатает результат."""
    match operation:
        case "+":
            print(f"{x} + {y} + {z} = {x + y + z}")
        case "-":
            print(f"{x} - {y} - {z} = {x - y - z}")
        case "/":
            print(f"{x} / {y} / {z} = {x / y / z}")
        case "*":
            print(f"{x} * {y} * {z} = {x * y * z}")
        case _:
            print(f"Invalid operation: {operation}")


repeat(testing_function)(4)
repeat(testing_function_1, 1, 6)(3)
repeat(testing_function_2, 1, 6, 8)()
repeat(testing_function_2, 1, 6, 8, operation="-")(1)
repeat(testing_function_2, 1, 6, 8, operation="*")(7)
repeat(testing_function_2, 1, 6, 8, operation="/")()

#  =========================
# Одна задача — один файл. Имя файла: <номер_задачи>.py
# Каждая функция должна быть документирована, её параметры и возвращаемое значение должны быть аннотированы.
# Работа функций проверяется в режиме инспекции файла с кодом.
# Ввод и вывод в стандартные потоки результатов проверки копируются.
# Копия в виде комментария помещается в конец файла с кодом задачи.
# Файлы с кодом упаковываются в архив. Имя файла архива: <фамилия>.zip|rar|7z|...

"""
>>> repeat(testing_function)(4)
python
python
python
python
>>> repeat(testing_function_1, 1, 6)(3)
1 + 6 = 7
1 + 6 = 7
1 + 6 = 7
>>> repeat(testing_function_2, 1, 6, 8)()
1 + 6 + 8 = 15
1 + 6 + 8 = 15
>>> repeat(testing_function_2, 1, 6, 8, operation="-")(1)
1 - 6 - 8 = -13
>>> repeat(testing_function_2, 1, 6, 8, operation="*")(7)
1 * 6 * 8 = 48
1 * 6 * 8 = 48
1 * 6 * 8 = 48
1 * 6 * 8 = 48
1 * 6 * 8 = 48
1 * 6 * 8 = 48
1 * 6 * 8 = 48
>>> repeat(testing_function_2, 1, 6, 8, operation="/")()
1 / 6 / 8 = 0.020833333333333332
1 / 6 / 8 = 0.020833333333333332

"""
