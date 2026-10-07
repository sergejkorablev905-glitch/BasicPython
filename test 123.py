# from unittest import result
#
# # import numpy as np
# # arr_1d = np.array([1, 2, 3, 4, 5])
# # print(arr_1d)
#
#
#
# # import numpy as np
# # arr_2d = np.array([
# # [1, 2, 3],
# # [4, 5, 6],
# # [7, 8, 9]
# # ])
# # print(arr_2d)
#
#
#
#
#
# #
# # import numpy as np
# # # Создаём номера строк: 0, 1, 2, ..., 7
# # line = np.arange(8)
# # # Создаём номера столбцов: 0, 1, 2, ..., 7
# # column = np.arange(8)
# # # Складываем номера строк и столбцов
# # # и берём остаток от деления на 2
# # matrix = (line[:, None] + column) % 2
# # # Выводим матрицу
# # print(matrix)
#
# # import numpy as np
# # # data = np.array([5 -3 0 8 -10 2 4 -1 7 -6])
# # # print(arr_1d)
# # data[data < 0] = 0        # Заменяем все отрицательные числа на 0 -> [12, 0, 0, 8, 0, 15]
# #
# #
# # print(data)
#
#
# # import numpy as np
# # data = np.array([5 -3 0 8 -10 2 4 -1 7 -6])
# # filtered = data[data < 0]
# # print(filtered)
#
# # import numpy as np
# # data = np.array([5, 12, 3, 8, 20, 15])
# # filtered = data[data > 10]
# # print("Отфильтрованные данные:", filtered)
#
#
# # import numpy as np
# # arr = input().split()
# # arr = list(map(int, arr))
# # arr = np.array(arr)
# # arr[arr < 0] = 0
# # print(arr)
#
#
# #
# # import numpy as np
# #
# # matrix = np.loadtxt("matrix.txt")#dtype=int)
# # result = np.sum(matrix, axis=0)
# # result1 = np.max(matrix, axis=1)
# #
# # print(result)
# # print (result1)
#
#
#
#
#
#
# # 3. Статистика матрицы
# # ##################################
# # Задание
# # Считайте из файла matrix.txt двумерный массив чисел (матрицу) размера 4x5.
# # Файл содержит ровно 4 строки, в каждой из которых записано по 5 чисел, разделенных пробелами.
# # Вычислите сумму элементов для каждого столбца отдельно и максимальное значение для каждой строки отдельно.
# # Формат входных данных
# # Текстовый файл matrix.txt, содержащий 4 строки по 5 чисел через пробел.
# # Формат выходных данных
# # На первой строке: массив сумм по столбцам формы (5,).
# # На второй строке: массив максимумов по строкам формы (4,).
# # РЕШЕНИЕ:
#
# # Подключаем библиотеку NumPy.
# # NumPy нужна нам для работы с массивами и матрицами,
# # а также для быстрого вычисления сумм и максимумов.
#
# # Считываем матрицу из файла "matrix.txt".
# # np.loadtxt() позволяет сразу прочитать числа из файла
# # и превратить их в массив NumPy.
#
# # Мы НЕ указываем dtype=int,
# # потому что по условию результат должен содержать вещественные числа: 34. 38. 42. и т.д. (
#
# # Считаем сумму элементов каждого столбца.
# # np.sum() — функция NumPy для вычисления суммы.
# # matrix — наша матрица, которую мы прочитали из файла.
# # axis=0 означает, что мы работаем по столбцам.
# # Например:
# # 1  2  3
# # 4  5  6
# # Получим:
# # 1 + 4 = 5
# # 2 + 5 = 7
# # 3 + 6 = 9
#
# # Находим максимальное значение в каждой строке.
# # np.max() — функция NumPy для поиска максимального значения.
# # matrix — наша матрица.
# # axis=1 означает, что мы работаем по строкам.
# # Например:
# # 1  2  3  → максимум 3
# # 4  5  6  → максимум 6
# # Получим:
# # [3. 6.]
#
# # Выводим на экран сумму каждого столбца.
#
# # Выводим на экран максимальное значение каждой строки.
#
#
# # Знакомство с библиотекой NumPy
# ##################################
# # 1. Шахматная доска из нулей и единиц
# # Задание
# # Сформируйте двумерный массив (матрицу) размера 8x8, состоящий из 0 и 1, заполнив его в шахматном порядке. Позиция [0, 0] должна содержать 0.
# # Формат входных данных
# # Входные данные отсутствуют.
# # Формат выходных данных
# # Двумерный массив NumPy размера (8, 8) с целочисленным типом int64 или int32
# РЕШЕНИЕ:
# #Подключаем библиотеку NumPy.
# # NumPy нужна нам для создания и обработки двумерного массива.
#
# # Создаём массив чисел от 0 до 7.
# # Эти числа будут обозначать номера строк нашей матрицы.
# # Получится: [0 1 2 3 4 5 6 7]
#
# # Ещё раз создаём числа от 0 до 7.
# # Теперь эти числа будут обозначать номера столбцов.
# # Получится: [0 1 2 3 4 5 6 7]
#
#
# # line[:, None] превращает массив строк
# # из горизонтального:
# # [0 1 2 3 4 5 6 7]
# #
# # в вертикальный:
# # [[0]
# #  [1]
# #  [2]
# #  [3]
# #  [4]
# #  [5]
# #  [6]
# #  [7]]
# #
# # Это нужно для того, чтобы NumPy смог
# # сложить каждый номер строки с каждым номером столбца.
# #
# # column при этом остаётся:
# # [0 1 2 3 4 5 6 7]
# #
# # В результате NumPy получает все возможные суммы:
# # 0+0  0+1  0+2 ...
# # 1+0  1+1  1+2 ...
# # 2+0  2+1  2+2 ...
# # и так далее.
# #
# # % 2 берёт остаток от деления каждой суммы на 2.
# # Чётные числа дают 0, нечётные дают 1.
# #
# # Именно поэтому получается шахматный порядок:
# # 0 1 0 1 ...
# # 1 0 1 0 ...
# #
# # Нам не нужен for, потому что NumPy
# # выполняет все эти действия сразу для всего массива.
#
# # Выводим получившуюся матрицу на экран.
#
#
# import numpy as np
# line = np.arange(8)
# column = np.arange(8)
# matrix = (line[:, None]+ column) %2
# print(matrix)

#======================================================================================================================
# Задача
# Загрузите данные об оценках студентов из файла grades.csv.
# Вычислите средний балл каждого студента по всем предметам и выведите имя студента с наивысшим средним баллом, а также сам балл (округленный до 2 знаков после запятой).
# Формат входных данных
# CSV-файл grades.csv (разделитель — запятая, кодировка UTF-8).
# Первая колонка обязательно называется student_name и содержит строковые имена студентов.
# Все последующие колонки содержат числовые оценки студентов (тип int или float) по различным учебным дисциплинам.
# Количество и названия колонок с предметами могут быть произвольными.
# В файле гарантированно присутствуют столбцы с именами и предметами.
# Формат выходных данных
# Две строки текста:
# Имя студента с наивысшим средним баллом
# Средний балл данного студента, округленный до 2 знаков после запятой




# # Подключаем библиотеку pandas для работы с таблицами
# import pandas as pd
#
# # Читаем таблицу с оценками студентов из CSV-файла
# df = pd.read_csv(
#     "txt.csv/grades.csv",  # Путь к файлу с оценками
#     encoding="utf-8",      # Указываем кодировку для правильного чтения текста
#     sep=","                # Указываем, что столбцы разделены запятыми
# )
#
# # Выбираем все столбцы с оценками, начиная со второго столбца
# # iloc[:, 1:] означает: все строки и столбцы с индексом 1 до конца
# # axis=1 означает, что считаем среднее значение по строкам
# # В результате получаем средний балл каждого студента
# average = df.iloc[:, 1:].mean(axis=1)
#
# # Находим самый высокий средний балл среди всех студентов
# # max() возвращает наибольшее значение
# best_average = average.max()
#
# # Находим всех студентов, у которых средний балл равен максимальному
# # average == best_average проверяет условие для каждого студента
# # df.loc выбирает строки, подходящие под условие
# # "student_name" указывает, что нам нужны только имена студентов
# best_students = df.loc[average == best_average, "student_name"]
#
# # Перебираем всех студентов, у которых максимальный средний балл
# # student — переменная, которая по очереди получает имя каждого студента
# for student in best_students:
#     # Выводим имя очередного студента
#     print(student)
#
# # Выводим максимальный средний балл
# # :.2f форматирует число, оставляя ровно два знака после запятой
# print(f"{best_average:.2f}")



# print(df)
# print("-"*100)
# print("Размер датасета:", df.shape)
#
# df.info()




# import pandas as pd
# products = pd.read_csv("txt.csv/products.csv",
#                        encoding="utf-8",
#                        )
# filtered_product = products.loc[
#     (products["category"] == "Electronics")&
#     (products["stock_quantity"] > 0)&
#     (products["price"] > 50000)
# ]
# print(filtered_product[["product_name", "price"]])



# 1. Самый высокий оклад в отделе



# import pandas as pd
#
# employees = pd.read_csv("txt.csv/salaries.csv",
#                         encoding="utf-8",
#                         sep=";",
#                         )
# row_index = employees['salary'].idxmax()
# name = employees.loc[row_index, "name"]
# department = employees.loc[row_index, "department"]
# salary = employees.loc[row_index, "salary"]
#
# print(f"Сотрудник: {name} | Отдел: {department} | Оклад: {salary:.2f}")

# (f"{best_average:.2f}")
# ]
# print(filtered_product[["product_name", "price"]])



# 2. Поиск отсутствующих цен в прейскуранте
#
# import pandas as pd
# # Подключаем библиотеку pandas для работы с таблицами и CSV-файлами.
#
#
# product_price_list = pd.read_csv(
#     "price_list.csv",
#     encoding="utf-8",
#     dtype={"price": "Int64"}
# )
# # Читаем файл price_list.csv и сохраняем таблицу в product_price_list.
# # encoding="utf-8" — указываем кодировку файла.
# # dtype={"price": "Int64"} — указываем, что price содержит целые числа,
# # но при этом разрешаем пропуски в этом столбце.
#
#
# missing_prices = product_price_list["price"].isna()
# # Берём столбец price.
# # isna() проверяет каждую ячейку:
# # True  — если цена отсутствует.
# # False — если цена указана.
#
#
# missing_count = missing_prices.sum()
# # Считаем количество пропусков.
# # True считается как 1, а False как 0.
# # Поэтому sum() даёт общее количество товаров без цены.
#
#
# missing_codes = product_price_list[missing_prices]["item_code"]
# # Оставляем только строки, где цена отсутствует.
# # Затем берём из этих строк только столбец item_code.
# # В результате получаем артикулы товаров без цены.
#
#
# missing_codes = missing_codes.astype(str)
# # Превращаем артикулы в строки.
# # Это нужно, чтобы потом объединить их через запятую.
#
#
# codes = ", ".join(missing_codes)
# # Объединяем все артикулы в одну строку.
# # ", " означает: между артикулами ставим запятую и пробел.
# # Например: 102, 104, 107.
#
#
# print(f"Пропусков цены: {missing_count}")
# # Выводим количество товаров, у которых нет цены.
#
#
# print(f"Артикулы: {codes}")
# # Выводим артикулы товаров с пропущенной ценой.


# import pandas as pd
#
# product_price_list = pd.read_csv(
#     "price_list.csv",
#     encoding="utf-8"
# )
#
# missing_prices = product_price_list["price"].isna()
#
# missing_count = missing_prices.sum()
#
# missing_codes = product_price_list[missing_prices]["item_code"]
#
# missing_codes = missing_codes.astype(str)
#
# codes = ", ".join(missing_codes)
#
# print(f"Пропусков цены: {missing_count}")
# print(f"Артикулы: {codes}")

# import pandas as pd
#
# # Читаем файл price_list.csv и сохраняем таблицу в переменную product_price_list
# product_price_list = pd.read_csv(
#     "price_list.csv",
#     encoding="utf-8"
# )
#
# # Проверяем столбец price и находим строки, где цена не указана
# missing_prices = product_price_list["price"].isna()
#
# # Считаем количество пропущенных цен
# missing_count = missing_prices.sum()
#
# # Оставляем только товары без цены и берём их артикулы
# missing_codes = product_price_list[missing_prices]["item_code"]
#
# # Преобразуем артикулы в строки
# missing_codes = missing_codes.astype(str)
#
# # Соединяем все артикулы через запятую и пробел
# codes = ", ".join(missing_codes)
#
# # Выводим количество пропущенных цен
# print(f"Пропусков цены: {missing_count}")
#
# # Выводим список артикулов
# print(f"Артикулы: {codes}")



# import pandas as pd
#
# product_price_list = pd.read_csv(
#     "txt.csv/price_list.csv",
#     encoding="utf-8"
# )
# missing_prices = product_price_list["price"].isna()
# missing_count = missing_prices.sum()
# missing_codes = product_price_list[missing_prices]["item_code"]
# missing_codes = missing_codes.astype(str)
# codes = ", ".join(missing_codes)
# print(f"Пропусков цены: {missing_count}")
# print(f"Артикулы: {codes}")


# import pandas as pd
#
# active_subscriptions = pd.read_csv(
#     "txt.csv/subscriptions.csv",
#     encoding="utf-8",
# )
# active_subscriptions['is_active'] = active_subscriptions['is_active'].astype('boolean')
# #active_subscriptions['is_active'] = active_subscriptions['is_active'].fillna(False).astype('bool') второй варик
# number_of_active = active_subscriptions["is_active"].sum()
# print(f"Активных подписок: {number_of_active}")


# print(f"Активных подписок: {number_of_active}")
#
# active_subscriptions.info()
# print("-"*100)
# print("Размер датасета:", active_subscriptions.shape)

# print(f"Активных подписок: {missing_count}")


# Автоматическая замена всех указанных маркеров на NaN
# import pandas as pd
# df = pd.read_csv("data.csv", na_values=["-", "missing", "N/A", "нет данных"])





# import pandas as pd
#
# dubious_loan_application = pd.read_csv(
#     "txt.csv/credit_applications.csv",
#     encoding="utf-8",
# )
# questionable_application = (
#     (dubious_loan_application["loan_amount"] > 1000000)
#     &
#     (dubious_loan_application["monthly_income"].isna())
# )
# age_condition = (
#     (dubious_loan_application["age"] < 18) |
#     (dubious_loan_application["age"] > 100)
# )
# suspicious = questionable_application | age_condition
# count_true = suspicious.sum()
# first_suspicious_id = dubious_loan_application.loc[suspicious, 'app_id'].iloc[0]
#
# print(f"Сомнительных заявок: {count_true}")
# print(f"Первая заявка ID: {first_suspicious_id}")



import pandas as pd

customer_inquiries = pd.read_csv(
    "txt.csv/call_logs.csv",
    encoding="utf-8",
    sep=","
)
number_of_rows = customer_inquiries.shape[0]
remove_duplicates = customer_inquiries.drop_duplicates(subset="call_id")
number_after_duplicates = remove_duplicates.shape[0]
deleted = number_of_rows - number_after_duplicates

print("Удалено дубликатов:", deleted)

















