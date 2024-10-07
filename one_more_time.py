from math import pi
class Figure:
    sides_count = 0

    filled = False

    newbie = True
    def __init__(self, color, *sides):
        self.__color = self.set_color(color)
        self.__sides = self.set_sides(sides)
        self.newbie = False




    def get_color(self):
        return self.__color

    def __is_valid_color(self, color):
        if all(isinstance(i, int) for i in color) and all(i in range(0, 256) for i in color):
            # print("Цвет правильный")
            return True
        else:
            # print("Цвет не правильный")
            return False

    def set_sides(self, *new_sides):

        if self.newbie:
            sides = new_sides[0]
            if self.__is_valid_sides(sides):
                self.__sides = list(sides)
                return self.__sides
            else:
                self.__sides = []
                for i in range(self.sides_count):
                    self.__sides.append(1)
                return self.__sides

        else:
            if self.__is_valid_sides(new_sides):
                self.__sides = list(new_sides)
                return self.__sides
    def set_color(self, *new_color):
        if self.newbie:
            color = new_color[0]
            if self.__is_valid_color(color):
                self.__color = list(color)
                return self.__color
        else:
            if self.__is_valid_color(new_color):
                self.__color = list(new_color)
                return self.__color



    def __is_valid_sides(self, sides):
        if all(isinstance(i, int) for i in sides) and all(i > 0 for i in sides) and self.sides_count == len(sides):
            return True
        else:
            return False



    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)




class Circle(Figure):
    sides_count = 1
    __radius = 0

    def radius(self):
        self.__radius = super().get_sides()[0] / 2 * pi
        return self.__radius

    def get_square(self):
        s_= pi*(self.__radius**2)
        return s_



class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        per_list = super().get_sides()
        per_ = (per_list[0] + per_list[1] + per_list[2]) / 2
        square_ = (per_ * (per_ - per_list[0]) * (per_ - per_list[1]) * (
                    per_ - per_list[2])) ** 0.5
        return square_




class Cube(Figure):
    sides_count = 12

    def set_sides(self, *new_sides):
        if self.newbie:
            if len(new_sides[0]) == 1:
                self.__sides = []
                sides = new_sides[0]
                for i in range(self.sides_count):
                    self.__sides.append(sides[0])
                return self.__sides
            else:
                return self.__sides
        else:
            if len(new_sides) == 1:
                self.__sides = []
                sides = new_sides[0]
                for i in range(self.sides_count):
                    self.__sides.append(sides)
                return self.__sides
            else:
                return self.__sides

    def get_sides(self):
        return self.__sides

    def get_volume(self):
        return super().get_sides()[0]**3



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
print(circle1.get_color())
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
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
print(circle1.radius())
print(circle1.get_square())


triangle1 = Triangle((50,50,50),10, 12, 13)
triangle1.set_color(20,30,40)
print(triangle1.get_sides())
print(triangle1.get_color())
print(triangle1.get_square())