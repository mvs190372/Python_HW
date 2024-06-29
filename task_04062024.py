# Доделать задачу с генерацией пароля.
import string
import random


CONST_MIN_PASSWORD_LENGTH = 10
CONST_MAX_PASSWORD_LENGTH = 30
CONST_MIN_PASSWORD_COMPLEXITY = 1
CONST_MIDDLE_PASSWORD_COMPLEXITY = 2
CONST_MAX_PASSWORD_COMPLEXITY = 3


def generate_password(length=CONST_MAX_PASSWORD_LENGTH, complexity=CONST_MAX_PASSWORD_COMPLEXITY):
    password = ""
    length = CONST_MIN_PASSWORD_LENGTH if length < CONST_MIN_PASSWORD_LENGTH else CONST_MAX_PASSWORD_LENGTH if length > CONST_MAX_PASSWORD_LENGTH else length
    # print(f"{length} - {complexity}")
    match complexity:
        case complexity if complexity == CONST_MIN_PASSWORD_COMPLEXITY:
            symbols = string.ascii_letters
        case complexity if complexity == CONST_MIDDLE_PASSWORD_COMPLEXITY:
            symbols = string.ascii_letters + string.digits
        case _:
            symbols = string.ascii_letters + string.digits + string.punctuation
    for _ in range(length):
        password += random.choice(symbols)
    return password


print("Для генерации случайного пароля введите длину пароля.")
print(f"Минимальная длина пароля - {CONST_MIN_PASSWORD_LENGTH}.")
print(f"Максимальная длина пароля - {CONST_MAX_PASSWORD_LENGTH}.")
print(f"Допустимые значения сложности пароля: {CONST_MIN_PASSWORD_COMPLEXITY} - только буквы, {CONST_MIDDLE_PASSWORD_COMPLEXITY} - буквы и цифры, {CONST_MAX_PASSWORD_COMPLEXITY} - буквы, цифры, спецсимволы.")
print("Если Вы укажете длину больше указанного диапазона, длина пароля будет приравнена к верхней границе диапазона.")
print("Если Вы укажете длину меньше указанного диапазона, длина пароля будет приравнена к нижней границе диапазона.")
print(f"Если Вы укажете недопустимое значение сложности, сложность пароля будет считаться равной {CONST_MAX_PASSWORD_COMPLEXITY}.")
print("*************************")
print("Примеры результатов вызова функции generate_password:")
print("generate_password(0):")
print(generate_password(0))
print("generate_password(20,):")
print(generate_password(20,))
print("generate_password(18, 1):")
print(generate_password(18, 1))
print("generate_password(15, 2):")
print(generate_password(15, 2))
print("generate_password(12, 3):")
print(generate_password(12, 3))
print("generate_password():")
print(generate_password())
print("*************************")


password_length = 0
while True:
    try:
        password_length = int(input("Введите длину пароля:"))
    except Exception as err:
        print("Ошибка ввода. Повторите ввод.")
        continue
    break
password_complexity = CONST_MAX_PASSWORD_COMPLEXITY
try:
    password_complexity = int(input("Введите сложность пароля:"))
except Exception as err:
    pass
print("Пароль:")
print(generate_password(password_length, password_complexity))


print("****************************************************************************************************")
print("Подсчет уникальных слов в тексте.")
# Задача "Подсчет уникальных слов в тексте"
# Напишите функцию, которая принимает текстовую строку и подсчитывает количество уникальных
# слов в этой строке (без учета регистра символов). Уникальные слова - это слова, которые
# встречаются только один раз. Функция должна вернуть словарь, в котором ключами являются
# уникальные слова, а значениями - количество их вхождений в тексте.
#
# "Python - это язык программирования, который позволяет разрабатывать различные приложения.
# Python имеет простой синтаксис и широкие возможности. При изучении Python важно уделять
# внимание пониманию основных концепций. Python - отличный выбор для начинающих программистов и
# опытных разработчиков."
#
# Этот текст содержит различные уникальные слова, повторяющиеся слова и знаки препинания,
# поэтому он будет хорошим набором данных для тестирования вашей функции. Вы можете использовать
# его для проверки правильности подсчета уникальных слов в тексте. Если у вас возникнут вопросы
# или пожелания по дальнейшему тестированию или улучшению функции, пожалуйста, дайте знать!

text = """Python - это язык программирования, который позволяет разрабатывать различные приложения.
Python имеет простой синтаксис и широкие возможности. При изучении Python важно уделять
внимание пониманию основных концепций. Python - отличный выбор для начинающих программистов
и опытных разработчиков."""
# text = "При работе со словарями у вас, возможно, возникал вопрос — а как добавить элемент в словарь. В этой статье вы найдете ответ."


def filter_unique(ls1):
    filtered = []
    for item in ls1:
        if ls1.count(item) == 1:
            filtered.append(item)
    return filtered


def filter_not_unique(ls1):
    filtered = []
    for item in ls1:
        if ls1.count(item) > 1:
            filtered.append(item)
    return filtered


def count_unique(text1):
    text2 = text1.lower()
    for i in range(len(string.punctuation)):
        text2 = text2.replace(string.punctuation[i], "")
    words = text2.split()
    unique = filter_unique(words)
    dictionary_unique = {}
    for item in unique:
        dictionary_unique[item] = words.count(item)
    return dictionary_unique


def count_not_unique(text1):
    text2 = text1.lower()
    for i in range(len(string.punctuation)):
        text2 = text2.replace(string.punctuation[i], "")
    words = text2.split()
    unique = filter_not_unique(words)
    dictionary_not_unique = {}
    for item in unique:
        dictionary_not_unique[item] = words.count(item)
    return dictionary_not_unique


print("Текст:")
print(text)
print(f"В тексте найдены следующие пары \"уникальное слово : количество повторений\": {count_unique(text)}")
print(f"В тексте найдены следующие пары \"НЕуникальное слово : количество повторений\": {count_not_unique(text)}")
print("****************************************************************************************************")
print("Магазин игрушек.")
# Задача "Магазин игрушек"
# В маленьком магазине игрушек "Веселые карусели" проходит акция для малышей.
# У каждого маленького покупателя есть возможность выбрать определенную игрушку
# со скидкой в зависимости от их возраста.
# Магазин предлагает следующие возрастные категории и скидки:
# Для детей до 3 лет - 10% скидка
# Для детей от 3 до 6 лет - 20% скидка
# Для детей от 6 до 10 лет - 30% скидка
# Для детей от 10 до 14 лет - 40% скидка
# Для детей старше 14 лет - 50% скидка
# В каждой категории скидка распространяется на все игрушки.
# Вам предстоит написать программу, которая с помощью функций, списков и оператора
# match case будет определять скидку для каждого покупателя в зависимости от их возраста.


children = [
    ("Alice", 1),
    ("Emily", 4),
    ("Bob", 7),
    ("Tom", 11),
    ("Charlie", 18),
    ("Stiven", 3),
]


def get_discount(child1):
    age = child1[1]
    match age:
        case age if age > 0 and age < 3:
            return [child1[0], age, 10]
        case age if age >= 3 and age < 6:
            return [child1[0], age, 20]
        case age if age >= 6 and age < 10:
            return [child1[0], age, 30]
        case age if age >= 10 and age < 14:
            return [child1[0], age, 40]
        case age if age >= 14 and age < 18:
            return [child1[0], age, 50]
        case _:
            return [child1[0], age, 0]


for child in children:
    child_info = get_discount(child)
    print(f"Посетитель: {child_info[0]}, возраст: {child_info[1]}, скидка: {child_info[2]}%")

# Задача "Турнир по дартсу"
# В джентльменском клубе "Мастера Дартса" проходит ежемесячный турнир по дартсу.
# Участникам предстоит соревноваться в меткости и точности бросков. Организаторы
# решили автоматизировать процесс подсчета очков с помощью специальной программы.
# У каждого участника есть возможность совершить 5 бросков в каждом раунде.
# За каждое попадание в мишень игрок получает определенное количество очков.
# В зависимости от набранных очков после 5 бросков игроки будут распределены по разным категориям.
# Создайте программу, используя функции, списки и оператор match case, которая
# будет определять категорию каждого игрока в турнире по их общему количеству очков после 5 бросков.
print("****************************************************************************************************")
print("Турнир по дартсу.")


def get_summa_category(player1):
    summa = sum(player1[1:])
    match summa:
        case summa if summa > 150:
            return [summa, 1]
        case summa if summa >= 100 and summa <= 150:
            return [summa, 2]
        case _:
            return [summa, 3]


players = [
    ("Alice", 20, 15, 10, 5, 12),
    ("Emily", 30, 35, 30, 5, 12),
    ("Bob", 35, 30, 30, 35, 30),
    ("Tom", 25, 15, 10, 15, 12),
    ("Charlie", 15, 15, 20, 25, 30),
    ("Stiven", 5, 5, 20, 25, 30),
]
players_info = []
for player in players:
    player_info = get_summa_category(player)
    players_info.append([player[0], player_info[0], player_info[1]])

players_info.sort(key=lambda x: x[2])
for player in players_info:
    print(f"{player[0]}: сумма очков за 5 бросков - {player[1]}, категория игрока - {player[2]}")
