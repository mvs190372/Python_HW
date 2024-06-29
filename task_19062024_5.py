# ПРОДВИНУТАЯ РАБОТА С ФУНКЦИЯМИ
# ==========  5  ==========
# Написать декоратор с именем logger, который в стандартном потоке вывода ведёт журнал вызовов
# декорируемой функции.
# В журнал необходимо внести имя вызванной функции и перечислить переданные аргументы. Ключевые
# аргументы должны быть перечислены с указанием ключа — имени параметра, в который эти аргументы
# передаются.
# Помимо переданных аргументов в журнал необходимо внести использованные значения по умолчанию.
# Значения по умолчанию доступны в специальных атрибутах объекта функции __defaults__ (позиционные)
# и __kwdefaults__ (ключевые)
# Количество объявленных в функции строго позиционных и позиционно-ключевых параметров доступно в
# атрибуте функции __code__.co_argcount
# В случае возникновения исключения его имя и текст также должны быть внесены в журнал, само
# исключение при перехвате игнорируется.
# Перехват любого исключения (в данном случае требуется перехватывать именно любое исключение, потому что
# декоратор может быть применён к произвольной функции) возможен при использовании базового класса Exception:
#     try:
#         int('a')
#     except Exception:
#         pass
#
#     Доступ к объекту исключения возможен при использовании конструкции as <переменная>:
#     try:
#         sorted(150)
#     except TypeError as exception:
#         print(exception)
# Имя объекта исключения доступно во встроенном атрибуте __name__. Текст исключения (без обратной
# трассировки) возвращается при получении строкового представления объекта исключения.
# В примере выше в stdout будет выведено: 'int' object is not iterable.
# Декоратор может применяться к функциям с различным набором позиционных и ключевых аргументов.
# Написанный декоратор необходимо протестировать вручную с помощью различных дополнительных произвольных функций.
# Пример ручного теста:
#     >>> def div_round(num1, num2, *, digits=0):
#     ...     return round(num1 / num2, digits)
#     ...
#     >>> div_round = logger(div_round)
#     >>>
#     >>>
#     >>> div_round(1, 3, digits=2)
#     div_round(1, 3, digits=2) -> 0.33
#     0.33
#     >>> div_round(7, 2)
#     div_round(7, 2, digits=0) -> 4.0
#     4.0
#     >>> div_round(5, 0)
#     div_round(5, 0, digits=0) .. ZeroDivisionError: division by zero
#     >>>
import sys


def logger(func: object) -> None:
    """Функция-декоратор для ведения журнала вызовов декорируемой функции."""
    def wrapper(*args, **kwargs):
        original_result = None
        err = ""
        try:
            original_result = func(*args, **kwargs)
        except Exception as e:
            err = str(e.__class__.__name__)
        data = f"{func.__name__}("
        temp = ""
        for arg in args:
            if temp != "":
                temp += ", "
            temp += f"{arg}"
        for key, value in kwargs.items():
            if temp != "":
                temp += ", "
            temp += f"{key}={value}"
        if len(kwargs) != func.__code__.co_kwonlyargcount:
            if temp != "":
                temp += ", "
            for key, value in func.__kwdefaults__.items():
                temp += f"{key}={value}"
        data += temp + ") "
        if err == "":
            data += f"-> {original_result}"
        else:
            data += f".. {err}"
        data += "\n"
        sys.stdout.write(data)

        return original_result

    return wrapper


def div_round(num1: float, num2: float, *, digits: int = 0) -> float:
    """Функция деления num1 На num2 с округлением до digits знаков."""
    return round(num1 / num2, digits)


logger(div_round)(1, 3, digits=2)
logger(div_round)(1, 3, digits=2.5)
logger(div_round)(7, 2)
logger(div_round)(5, 0)


#  =========================
# Одна задача — один файл. Имя файла: <номер_задачи>.py
# Каждая функция должна быть документирована, её параметры и возвращаемое значение должны быть аннотированы.
# Работа функций проверяется в режиме инспекции файла с кодом.
# Ввод и вывод в стандартные потоки результатов проверки копируются.
# Копия в виде комментария помещается в конец файла с кодом задачи.
# Файлы с кодом упаковываются в архив. Имя файла архива: <фамилия>.zip|rar|7z|...

"""
>>> logger(div_round)(1, 3, digits=2)
div_round(1, 3, digits=2) -> 0.330.33
>>> logger(div_round)(1, 3, digits=2.5)
div_round(1, 3, digits=2.5) .. TypeError
>>> logger(div_round)(7, 2)
div_round(7, 2, digits=0) -> 4.04.0
>>> logger(div_round)(5, 0)
div_round(5, 0, digits=0) .. ZeroDivisionError
"""