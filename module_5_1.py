#Цель: применить на практике знания о классах, объектах и их атрибутах.
#Задача "Developer - не только разработчик":
#Реализуйте класс House, объекты которого будут создаваться следующим образом:
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        print(f"______________\n  Здание {self.name} из {self.number_of_floors} этажей \nПоднимаемся на {new_floor}-й")
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f"{new_floor} - такого этажа не существует")
        else:
            for floor in range(new_floor):
                print(floor + 1)

h1 = House('ЖК "Горский"', 18)
h2 = House('ЖК "Домик в деревне"', 5)
h3 = House('ЖК "Эльбрус"', 30)
h1.go_to(5)
h2.go_to(10)
h3.go_to (11)