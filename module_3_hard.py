#1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99
#Входные данные (применение функции):
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(data_structure):
    sum_ = 0  #  создание переменной со значением -  0
    for simb in data_structure: #  перебор всех элементов:
        if isinstance(simb, int):  # для числа
            sum_ += simb  #   + число
        elif isinstance(simb, str):  # для строки
            sum_ += len(simb)  # + длина строки
        elif isinstance(simb, list) or isinstance(simb, tuple): # для списка or кортежа
            sum_ += calculate_structure_sum(simb)  # рекурсия для распаковки списков или кортежей
        elif isinstance(simb, dict):  # для словаря
            sum_ += calculate_structure_sum(list(simb.keys()))  # рекурсия для словаря (ключи)
            sum_ += calculate_structure_sum(list(simb.values()))  # рекурсия для словаря (значения)
        elif isinstance(simb, set):  # для множества
            sum_ += calculate_structure_sum(simb)  # рекурсия для распаковки множества
    return sum_  #  возврат суммы

result = calculate_structure_sum(data_structure)
print("Сумма чисел и количества символов:",result)

#Выходные данные (консоль):
#99

