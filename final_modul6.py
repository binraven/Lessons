"""
Дополнительное практическое задание по модулю: "Наследование классов."

Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности

Задание "Они все так похожи":
# module6hard.py
"""

from math import pi
class Figure:
    side_count = 0
    filled = False

    def __init__(self,  color, *side_counts):
        self.__color = []
        self.__sides = []
        self.flag_new = True
        self.__is_valid_sides(*side_counts)
        self.set_color(color)
        self.check_sides = self.__is_valid_sides(*side_counts)
        if self.check_sides:
            self.set_sides(*side_counts)
        else:
            self.set_sides()
            #print("error sides")

    def get_color(self):
        if len(self.__color):
            return self.__color

    def set_color(self, color):
        if all(i >= 0 for i in color) and all(i <= 255 for i in color):
            self.__color = color

    def __is_valid_sides(self, *side_counts):
        if isinstance(self, Circle):
            if len(side_counts) == self.sides_count:
                self.flag_new = False
                return True
            else:
                if self.flag_new:
                    #print("New __is_valid_sides")
                    self.flag_new = False
                    self.__sides = [1]

                return False
        elif isinstance(self, Cube) :
            if len(side_counts) ==1:
                self.flag_new = False
                return True
            else:
                self.flag_new = False
                return False
        elif isinstance(self, Triangle):
            if len(side_counts) == 1 or len(side_counts) ==3:
                self.flag_new = False
                return True
            else:
                self.flag_new = False
                return False


    def get_sides(self):
        return self.__sides


    def set_sides(self, *new_sides):
        if isinstance(self, Cube) and new_sides != () and len(new_sides) == 1:
            temp_side_list = []
            self._Cube__valume = new_sides[0]
            for i in range (self.sides_count):
                temp_side_list.append(new_sides[0])
            self.__sides = temp_side_list
            self.flag_new = False
        elif isinstance(self, Circle):

            if len(new_sides) == 0:
                self.__sides = [1]
            else:
                self.__sides = list(new_sides)
                if isinstance(self, Circle):
                    # print(self.__sides)
                    len_ = self.__sides[0]
                    self._Circle__dlina = self.__sides[0]
                    self._Circle__radius = (len_ / (2 * pi))
                    self.flag_new = False

        elif isinstance(self, Triangle) and new_sides != () and len(new_sides) == 1:
            temp_side_list = []
            self._Cube__valume = new_sides[0]
            for i in range(self.sides_count):
                temp_side_list.append(new_sides[0])
            self.__sides = temp_side_list
            self._Triangle__per_list = temp_side_list
            self.flag_new = False

        elif isinstance(self, Triangle) and new_sides != () and len(new_sides) == 3:
            temp_side_list = []
            self._Cube__valume = new_sides[0]
            for i in range(self.sides_count):
                temp_side_list.append(new_sides[i])

            self.__sides = temp_side_list
            self._Triangle__per_list = temp_side_list
            self.flag_new = False



        if isinstance(self, Cube) and new_sides == ():
            temp_side_list = []
            for i in range(12):
                temp_side_list.append(1)
            self.__sides = temp_side_list
            self.flag_new = False
            self._Cube__valume = 1


class Circle (Figure):
    sides_count = 1

    def __init__(self, color, *side_counts):
        super().__init__(color, *side_counts)



    def get_square(self):
        s_= pi*(self.__radius**2)
        print( s_)

    def radius(self):
        return print(self.__radius)

    def __len__(self):
        return self.__dlina

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *side_counts):
        super().__init__(color, *side_counts)


    def get_volume(self):
        return self._Cube__valume**3

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *side_counts):
        super().__init__(color, *side_counts)

    def get_square(self):
        per_ = (self.__per_list[0] + self.__per_list[1] + self.__per_list[2]) / 2
        square_ = (per_*(per_-self.__per_list[0])*(per_-self.__per_list[1])*(per_-self.__per_list[2]))**0.5
        return square_


"""
Измнение цвета происходит если его передать в тюпле, т.е. картеже
circle1.set_color((55, 66, 77))

"""

# triangle1 = Triangle((50,50,50),10, 11, 12)
# triangle1.set_color((20,30,40))
# print(triangle1.get_sides())
# print(triangle1.get_square())
# print(triangle1.get_color())

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color((55, 66, 77)) # Изменится
print(circle1.get_color())
cube1.set_color((300, 70, 15)) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())