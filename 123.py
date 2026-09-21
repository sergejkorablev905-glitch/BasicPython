from operator import truediv
from typing import cast

# def get_word_stats(word):

cast(, ....)
#     count = len(word)
#     vowels = 0
#    consonants = 0
#
#     for c in word:
#                if c in 'аеёиоуыэюя':
#
#
#            wels += 1
#         elif c in 'бвгджзйклмнпрстфхцчшщ':
#             consonants += 1
#
#     return (count, vowels, consonants)



with open("salaries.txt", "r", encoding="utf-8") as f:
    header = next(f)

    with open("highly_paid.txt", "w", encoding="utf-8") as out:
        for line in f:
            data = line.strip().split()
            salary = int(data[3])

            if salary > 60000:
                res = data[0] + " " + data[1][0] + "." + data[2][0] + "."
                out.write(res + "\n")






