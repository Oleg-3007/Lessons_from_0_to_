rades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Джонни', 'Бильбо', 'Стив', 'Хендрик', 'Аарон'}
students_= list(students)           # преобразуем множество в список
students_.sort()                    # сортировка по алф.  #print (students_)
a = sum (rades [0])/len (rades [0]) # считаем ср. балл
b = sum (rades [1])/len (rades [1])
c = sum (rades [2])/len (rades [2])
d = sum (rades [3])/len (rades [3])
e = sum (rades [4])/len (rades [4])                     ## print (a, b, c, d, e)
average_score = [a, b, c, d, e]                         # создаем список "Средний балл"
result = dict(zip(students_, average_score))            # конвертируем 2 списка в словарь
print(result)