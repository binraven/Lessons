from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

        

    def run(self):
        print(f"{self.name}, на нас напали!")
        sopernik = 100
        day_fight = 1
        while not sopernik <= 0:

            sopernik -= self.power
            print(f"{self.name} сражается {day_fight}..., осталось {sopernik} воинов.")
            day_fight += 1
            sleep(1)
        return print(f"{self.name} одержал победу спустя {day_fight-1} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()