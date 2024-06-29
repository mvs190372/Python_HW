import pandas as pd
import matplotlib.pyplot as plt
import os
import openpyxl
import math
import pandas as pd

# Задача:
# Есть входной excel файл в котором находятся колонки:
# 1. ФИО
# 2. Набранный учеником балл
#
# Необходимо создать сводную таблицу в которой для каждого ученика вычисляется оценка по 12-и бальной шкале.
# (формулу можно найти в методе класса RateUtils - __to_rate_system())
#
# Так же необходимо создать функцию которая генерирует и показывает график итоговых оценок.
#
# Библиотеки которые я использовал:
# numpy - для проверки что в ячейке не нулевое значение.
# pandas - для работы с excel таблицами
# matplotlib - для генерации графиков.
# pandas


# def show_exam_results(path_to_xlsx_file):
#     wb = openpyxl.load_workbook(path_to_xlsx_file)
#     sheet = wb["Лист1"]
#     i = 0
#     x, y, z = [], [], []
#     while True:
#         i += 1
#         if sheet[f"A{i}"].value is None:
#             break
#         full_fio = str(sheet[f"A{i}"].value).split(" ")
#         fio = full_fio[0][0] + full_fio[1][0] + full_fio[2][0]
#         x.append(fio)
#         # формулу можно найти в методе класса RateUtils - __to_rate_system() - я плохо искала и не нашла,
#         # поэтому использовала формулу проще:
#         y.append(math.ceil(int(sheet[f"B{i}"].value)*12/100))
#     plt.xlabel('Ученики')
#     plt.ylabel('Оценки')
#     plt.title("Результаты экзамена в группе Python333")
#     # Необходимо создать сводную таблицу в которой для каждого ученика вычисляется оценка по 12-и бальной
#     # шкале:
#     df = pd.DataFrame({
#         'Ф.И.О.': x,
#         'Оценки': y
#     })
#     plt.plot(df["Ф.И.О."], df["Оценки"])
#     plt.show()
#
#
# show_exam_results(os.getcwd() + "\\Data\\Test\\Exam.xlsx")



# Задача: Анализ текстовых данных с использованием функционального подхода
# Вам необходимо разработать программу для анализа текстовых данных из нескольких файлов.
# Каждый файл содержит текстовую информацию о продажах определенного товара в разные периоды времени.
# Вам нужно выполнить следующие шаги с использованием функционального подхода:
# 1. Чтение данных:
#    Напишите функцию read_file(file_path), которая принимает путь к файлу и возвращает содержимое
#    файла в виде списка строк.
# 2. Обработка данных:
#    Напишите функцию process_data(data), которая принимает список строк с данными о продажах и
#    преобразует их в удобный формат (например, словарь с информацией о продажах для каждого периода времени).
# 3. Фильтрация данных:
#    Напишите функцию filter_data(data, threshold), которая принимает обработанные данные и пороговое
#    значение threshold для фильтрации. Функция должна вернуть только те записи о продажах, у которых
#    объем продаж превышает threshold.
# 4. Агрегация данных:
#    Напишите функцию aggregate_data(data), которая принимает отфильтрованные данные и агрегирует
#    их, например, вычисляя суммарный объем продаж по всем периодам времени.
# 5. Визуализация результатов:
#    Напишите функцию visualize_data(aggregated_data), которая принимает агрегированные данные и
#    визуализирует их, например, строит график или диаграмму.
# 6. Общий процесс:
#    Напишите основную функцию, которая объединяет все вышеперечисленные шаги и применяет их ко
#    всем файлам с данными о продажах.
# Эта задача поможет вам попрактиковаться в использовании функциональных подходов к обработке данных
# на Python, таких как отображение, фильтрация и свертка, а также в работе с файлами, структурами
# данных и визуализацией результатов.
# PS: Для работы с фалами используем open(). Не забываем закрывать файл в конце.


path_to_csv_files = os.getcwd() + "\\Data_11062024"
data = []
str_data = []


def process_data(lines) -> list:
    dictionary = {}
    result = []
    for line in lines:
        values = line.split(";")
        dictionary["country"] = values[0].strip()
        dictionary["product"] = values[1].strip()
        dictionary["units_sold"] = values[2].strip()
        dictionary["manufactoring_price"] = values[3].strip()
        dictionary["sale_price"] = values[4].strip()
        dictionary["date"] = values[5].strip()
        result.append(dictionary)
    return result


def get_data(file_path, file_name):
    full_file_path = f"{file_path}\\{file_name}"
    list_of_lines = read_file(full_file_path)
    return [list_of_lines, process_data(list_of_lines)]


def get_data_from_csv_files_inside_path(path):
    pattern = '.csv'
    result0 = []
    result1 = []
    os.chdir(path)
    for name in os.listdir(path):
        if os.path.isdir(name):
            continue
        else:
            if name.endswith(pattern):
                data_from_1_file = get_data(path, name)
                for result in data_from_1_file[0]:
                    result0.append(result)
                for result in data_from_1_file[1]:
                    result1.append(result)

    return [result0, result1]

def read_file(full_name) -> list:
    result = []
    with open(full_name, 'r') as f:
        for line in f:
            result.append(line.strip("\n"))
        f.close()
    return result


def filter_data(data1, threshold) -> list:
    filtered_data = []
    for item in data1:
        if float(item["units_sold"]) > threshold:
            filtered_data.append(item)
    return filtered_data


def aggregate_data(data1: list) -> list:
    aggregated_data = []
    periods = []
    for item in data1:
        if item["date"] not in periods:
            periods.append(item["date"])
    for period in periods:
        data_in_period = list(filter(lambda it: it["date"] == period, data1))
        summa = 0
        for ite in data_in_period:
            summa += float(ite["units_sold"])
        temp = {"date": period, "units_sold": summa}
        aggregated_data.append(temp)
    return aggregated_data


def visualize_data(aggregated_data):
    x, y = [], []
    for data in aggregated_data:
        x.append(data["date"][3:5])
        y.append(data["units_sold"])
    plt.bar(x, y, color='coral')
    plt.xlabel('Месяцы')
    plt.ylabel('Продано товаров')
    plt.title('Показатели продаж за 2014 год (помесячно)')
    plt.show()

def process_files(path_to_data):
    data = get_data_from_csv_files_inside_path(path_to_data)
    print("Данные, считанные из обрабатываемых файлов построчно:")
    print(data[0])
    print("Данные, считанные из обрабатываемых файлов в виде списка словарей:")
    print(data[1])
    threshold = 1000
    print(f"Пороговое значение объема продаж - {threshold}.")
    print("Данные, где объем продаж больше порогового значения:")
    data_more_threshold = filter_data(data[1], threshold)
    print(data_more_threshold)
    print("Данные по объемам продаж, сгруппированные по периодам времени:")
    data_group_by_date = aggregate_data(data_more_threshold)
    print(data_group_by_date)
    print("Визуализация агрегированных данных ->")
    visualize_data(data_group_by_date)


print("Анализ текстовых данных с использованием функционального подхода.")
print(f"Обработка файлов данных в директории {path_to_csv_files}.")
process_files(path_to_csv_files)