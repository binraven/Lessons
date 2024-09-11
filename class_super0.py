"""
Цель: закрепить знания множественного наследования в Python.

Задача "Мифическое наследование":

#module_6_3
"""
class Horse:
    sound = "Frrr"
    x_distance = 0
    def run(self, dx):
        self.x_distance = self.x_distance + dx
        return self.x_distance

    def voice(self):
        return print( f"{super().sound}")




class Eagle:
    sound = 'I train, eat, sleep, and repeat'
    y_distance = 0



    def fly(self, dy):
        self.y_distance = self.y_distance + dy
        return self.y_distance


class Pegasus (Horse, Eagle):
    pos = ()

    def __init__(self):
        self.pos = (super().x_distance, super().y_distance)

    def move(self, dx, dy):
        self.pos =(super().run(dx), super().fly(dy))
        return self.pos

    def get_pos(self):
        return self.pos


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

