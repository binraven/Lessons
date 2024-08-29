# "Атрибуты и методы объекта."
# Цель: применить на практике знания о классах, объектах и их атрибутах.
#
# Задача "Developer - не только разработчик"
# module_5_1
from time import sleep

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует\n")
        else:
            for i in range (1, new_floor+1):
                sleep(1)
                if i == new_floor:
                    print(f"Вы приехали на <<{i}>> этаж в доме *** {self.name} ***\n")
                else:
                    print(i)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)