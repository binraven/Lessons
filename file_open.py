"""
Цель: закрепить знания о работе с файлами (чтение/запись) решив задачу.

Задача "Учёт товаров":

#module_7_1.py
"""


class Shop:
    __file_name = "products.txt"

    def get_products(self):
        file = open(self.__file_name, "r")
        file_product = file.read()
        file.close()
        return file_product
    def add(self, *products):
        file_product = self.get_products()
        for i in products:
            if str(i) in file_product:
                print(f"Продукт {i} уже есть в магазине")
            else:
                file = open(self.__file_name, "a")
                file.write(f"{str(i)}\n" )
                file.close()

    
class Product ():
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category        

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
