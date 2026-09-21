
with open("numbers.txt", "r", encoding="utf-8") as f:
    text = f.read()

numbers = list(map(int, text.split()))


total = 0
count = 0

for number in numbers:
    total = total + number
    count = count + 1

average = total / count

print(total, f"{average:.2f}")



# Открываем файл numbers.txt для чтения.
# "r" означает read — чтение.
# encoding="utf-8" задаёт кодировку файла.
# as f — сохраняем открытый файл в переменную f.
with open("numbers.txt", "r", encoding="utf-8") as f:

    # Читаем всё содержимое файла целиком
    # и сохраняем его в переменную text.
    text = f.read()


# Разделяем весь текст на отдельные строки/значения.
# text.split() превращает текст:
# "-15\n25\n-5\n10\n-30"
# в список:
# ["-15", "25", "-5", "10", "-30"]
#
# int превращает каждую строку в целое число.
# list собирает полученные числа в список.
numbers = list(map(int, text.split()))


# Создаём переменную total для хранения суммы.
# В начале сумма равна 0, потому что
# мы ещё ничего не сложили.
total = 0


# Создаём переменную count для подсчёта количества чисел.
# В начале количество равно 0.
count = 0


# Перебираем все числа из списка numbers по одному.
# number — это текущее число.
for number in numbers:

    # Добавляем текущее число к общей сумме.
    total = total + number

    # Увеличиваем количество обработанных чисел на 1.
    count = count + 1


# Находим среднее арифметическое.
# Для этого сумму делим на количество чисел.
average = total / count


# Выводим сумму и среднее арифметическое.
# :.2f означает:
# показать среднее число с двумя знаками после точки.
print(total, f"{average:.2f}")

