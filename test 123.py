
# import numpy as np
# arr_1d = np.array([1, 2, 3, 4, 5])
# print(arr_1d)



# import numpy as np
# arr_2d = np.array([
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]
# ])
# print(arr_2d)





#
# import numpy as np
# # Создаём номера строк: 0, 1, 2, ..., 7
# line = np.arange(8)
# # Создаём номера столбцов: 0, 1, 2, ..., 7
# column = np.arange(8)
# # Складываем номера строк и столбцов
# # и берём остаток от деления на 2
# matrix = (line[:, None] + column) % 2
# # Выводим матрицу
# print(matrix)

# import numpy as np
# # data = np.array([5 -3 0 8 -10 2 4 -1 7 -6])
# # print(arr_1d)
# data[data < 0] = 0        # Заменяем все отрицательные числа на 0 -> [12, 0, 0, 8, 0, 15]
#
#
# print(data)


# import numpy as np
# data = np.array([5 -3 0 8 -10 2 4 -1 7 -6])
# filtered = data[data < 0]
# print(filtered)

# import numpy as np
# data = np.array([5, 12, 3, 8, 20, 15])
# filtered = data[data > 10]
# print("Отфильтрованные данные:", filtered)


# import numpy as np
# arr = input().split()
# arr = list(map(int, arr))
# arr = np.array(arr)
# arr[arr < 0] = 0
# print(arr)



import numpy as np

matrix = np.loadtxt("matrix.txt")#dtype=int)
result = np.sum(matrix, axis=0)
result1 = np.max(matrix, axis=1)

print(result)
print (result1)
