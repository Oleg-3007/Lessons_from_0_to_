#Цель: понять как работают базовые магические методы на практике.
#Задача "Магические здания":

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f"Название: {self.name}, кол-во этажей: {self.number_of_floors}")


h1 = House('ЖК "Горский"', 18)
h2 = House('ЖК "Домик в деревне"', 5)
h3 = House('ЖК "Эльбрус"', 24)


# __str__
print(h1)
print(h2)
print(h3)
print("=" * 20)
# __len__
print(len(h1))
print(len(h2))
print(len(h3))