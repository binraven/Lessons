import threading
from threading import Lock
from time import sleep
from random import randint

class Bank():

    def __init__(self):
        self.lock = Lock()
        self.balance = 0

    def deposit(self):
        for i in range(100):
            if self.lock.locked():
                self.lock.release()
            random_plus = randint(50, 501)
            self.balance += random_plus
            print(f"Пополнение: {random_plus}. Баланс: {self.balance}")

            sleep(0.001)
        return self.balance


    def take(self):
        for i in range(100):
            random_minus = randint(50, 501)
            if random_minus > self.balance:
                print("Запрос отклонён, недостаточно средств")

                self.lock.acquire()

            else:
                self.balance -= random_minus
                print(f"Снятие: {random_minus}. Баланс: {self.balance}")

            sleep(0.001)
        return self.balance


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
