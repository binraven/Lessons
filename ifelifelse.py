# "Условная конструкция. Операторы if, elif, else."
print("Введите 3 целых числа")
first = int(input("1 число: "))
second = int(input("2 число: "))
third = int(input("3 число: "))

if first != second and first != third and second != third:
    print("0")
elif first == second and first == third and second == third:
    print("3")
else:
    print("2")