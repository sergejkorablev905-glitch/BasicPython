name = "Сергей"
age = 43
template = f"Приветствую Вас {name} ваш возраст {age} лет"
print(template)


name = "Сергей"
age = 43
salary = 12.452
template = f"Приветствую Вас {name} ваш возраст {age} лет". Зарплата:{salary }
print(template)



employees = ["Алексей","Мария","Илья","Анна"]
print (employees[4])   #(employees[:3])  #(employees[1:3:2])



my_list = [23,"hello",2:45,true]
print(len(my_list))    # показывает колличество символов



salary = [10_000, 5_000, 12_000, 2_500]
print(max(salary))

employees = ["Алексей","Мария","Илья","Анна"]
print(max(employees))  #по порядку в алфавите в данном случае Мария

employees = ["Алексей","Мария","Илья","Анна"]
print(min(employees))  #по порядку в алфавите в данном случае Алексей


tuple - () кортеж можно и без скобок обязательно наличие запятой
employees = ("Алексей","Мария","Илья","Анна")
employees = "Алексей","Мария","Илья","Анна"
print(type(employees))

[] список

Множества: {set} фигурные скобки


set1 = {1, 2, 3}
set2 = (3, 4, 5}
intersection_set = set2 - set1
print (difference_set)

employees = ["Алексей","Мария","Илья","Анна","Мария","Илья"]
uniq_employees = set(employees)
print (uniq_employees)
