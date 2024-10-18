from threading import Thread
from time import sleep
from random import randint
import queue

class Table():
    def __init__(self, int):
        self.number = int
        self.guest = None


class Guest(Thread):
    def __init__(self, str):
        super().__init__()
        self.name = str
        self.run()


    def run(self):
        pause = randint(3, 11)
        sleep(0.001)


class Cafe():
    list_thread = []
    def __init__(self, *args):
        self.tables = list(args)
        self.queue = queue.Queue()


    def guest_arrival(self, *guests):
        list_guest = list(guests)
        empty_tables = []
        for guest in list_guest:
            empty_tables = [table for table in self.tables if table.guest == None]
            if len(empty_tables) != 0:
                empty_tables[0].guest = guest
                guest.start()
                self.list_thread.append(guest)
                print(f"Гоость {guest.name} сел за стол {empty_tables[0].number}")
            else:
                self.queue.put(guest)
                print(f"Гость {guest.name} помещен в очередь")

    def discuss_guests(self):
        empty_tables = []
        empty_tables = [table for table in self.tables if table.guest == None]
        while not self.queue.empty() or len(empty_tables) != 0:
            empty_tables = [table for table in self.tables if table.guest == None]
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f"{table.guest.name} за столом {table.number} покушал(-а) и ушёл(ушла)")
                    table.guest = None
                    if not self.queue.empty():
                        table.guest = self.queue.get()
                        table.guest.start()
                        print(f"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")



# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

for thr in Cafe.list_thread:
    thr.join()


