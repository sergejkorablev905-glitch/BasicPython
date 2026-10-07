# #import numpy as np
# import pandas as pd  # pip install pandas
#
# # Исходный массив NumPy
# # grades = np.array([
# #     [80, 90, 85],
# #     [70, 75, 80],
# #     [95, 85, 90],
# #     [60, 65, 70]
# # ])
#
# df_grades = pd.DataFrame(
#     data=grades,
#     index=["Alex", "Jordan", "Taylor", "Morgan"],
#     columns=["Math", "Science", "English"]
# )
#
# print(df_grades["Math"])
from operator import index

# import pandas as pd
# scores = pd.Series(
# [80, 90, 85],
# index=["Math", "English", "Science"]
# )


# import pandas as pd
# alex_grades = pd.Series({
#     "Math": 80,
#     "Science": 90,
#     "English": 85
# })
#
# print(alex_grades["Math"])
# print(alex_grades.loc["Math"])





# import pandas as pd
#
# salaries = pd.Series (
#     [1000, 3500.5, 2500, 3200.25],
#     index=["Alex", "Ann", "Mark", "Peter"]  # Каждое имя в своих кавычках
# )
# print (salaries[["Alex", "Ann", "Mark"]])
#


import pandas as pd
# data = {
#     "Math": [80, 70, 95, 60],
#     "Science": [90, 75, 85, 65],
#     "English": [85, 80, 90, 70]
#     },
# index=["Alex", "Jordan", "Taylor", "Morgan"]
# )
#     math_scores = df["Math"]
#     stem_scores = df[["Math", "Science"]]




# import pandas as pd
# students_data = [
# {"Math": 80, "Science": 90, "English": 85}, # Alex
# {"Math": 70, "Science": 75, "English": 80}, # Jordan
# {"Math": 95, "Science": 85, "English": 90}, # Taylor
# {"Math": 60, "Science": 65, "English": 70} # Morgan
# ]
# df = pd.DataFrame(
# students_data,
# index=["Alex", "Jordan", "Taylor", "Morgan"]
# )


# import pandas as pd
#
# # Создаем базовый DataFrame с оценками
# df = pd.DataFrame(
#     data={
#         "Math": [80, 70, 95, 60],
#         "Science": [90, 75, 85, 65],
#         "English": [85, 80, 90, 70]
#     },
#     index=["Alex", "Jordan", "Taylor", "Morgan"]
# )

# =====================================================================









# 1. Одна пара скобок: df["Math"] — Передаем СТРОКУ "Math"
# =====================================================================
# res_series = df["Math"]
#
# print("--- 1. Результат df['Math'] ---")
# print(res_series)
# print("\nТип объекта:", type(res_series))  #
# print("Размерность (shape):", res_series.shape)  # (4,) — одномерный массив!
#
# print("\n" + "="*50 + "\n")

# =====================================================================
# 2. Две пары скобок: df[["Math"]] — Передаем СПИСОК ['Math']
# =====================================================================
# res_dataframe = df[["Math"]]
#
# print("--- 2. Результат df[['Math']] ---")
# print(res_dataframe)
# print("\nТип объекта:", type(res_dataframe))
# print("Размерность (shape):", res_dataframe.shape)




# df = pd.DataFrame(
# data={
# "Math": [80, 70, 95, 60],
# "Science": [90, 75, 85, 65],
# "English": [85, 80, 90, 70]
# },
# index=["Alex", "Jordan", "Taylor", "Morgan"]
# )
# res_series = df["Math"]
# res_dataframe = df[["Math"]]

# print(res_dataframe)




import pandas as pd
df = pd.read_csv(
    "txt.csv/students_data.csv",
    index_col=0, sep=",", na_values=["-"],
    dtype={"math_score": "Int64", "science_score": "Int64", "is_active": "boolean"})

print(df)
print("-"*100)
print("Размер датасета:", df.shape)

df.info()

