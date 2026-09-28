# import sys
# import numpy as np
# import time
#
# SIZE = 10_000_000
#
# # Подготовка данных
# py_list1 = list(range(SIZE))
# py_list2 = list(range(SIZE))
#
# np_arr1 = np.arange(SIZE)
# np_arr2 = np.arange(SIZE)
#
# # --- 1. Сложение чистых списков Python (через list comprehension) ---
# start_time = time.time()
# py_result = [x + y for x, y in zip(py_list1, py_list2)]
# py_time = time.time() - start_time
#
# # --- 2. Векторное сложение в NumPy ---
# start_time = time.time()
# np_result = np_arr1 + np_arr2
# np_time = time.time() - start_time
#
# # --- Результаты ---
# print(f"Время выполнения на Python lists: {py_time:.5f} сек")
# print(f"Время выполнения на NumPy:       {np_time:.5f} сек")
# print(f"NumPy быстрее в {py_time / np_time:.1f} раз!")



# import numpy as np
# array = np.array([
#     [2, 4, 6],
#     [2, 4, 6],
#     [2, 4, 6],
# ], dtype=np.int16
# print (array.dtype)
# print (array.itimesize)




# import numpy as np
#
# # Диапазон для 16-битных целых чисел (int16)
# info_16 = np.iinfo(np.int16)
# print("int16:")
# print(f"  Минимум: {info_16.min}")
# print(f"  Максимум: {info_16.max}")
#
# # Диапазон для 64-битных целых чисел (int64)
# info_64 = np.iinfo(np.int64)
# print("\int64:")
# print(f"  Минимум: {info_64.min}")
# print(f"  Максимум: {info_64.max}")



import numpy as np

# Вариант 1: Стандартный Python (требуются циклы или list comprehension)
data = [1, 2, 3, 4, 5]
res_python = [x * 2 + 5 for x in data]

# Вариант 2: NumPy (запись выглядит как обычная математическая формула)
arr = np.array([1, 2, 3, 4, 5])
res_numpy = arr * 2 + 5

print("Python:", res_python)
print("NumPy:", res_numpy)