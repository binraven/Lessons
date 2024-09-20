"""
Цель: понять как работают исключения внутри функций и как обрабатываются эти исключения на практике при помощи try-except.

Задача "План перехват":

#module_8_2
"""
per_sum = 0
result = 0
def  personal_sum(numbers):
    global per_sum, result
    per_sum = 0
    result = 0
    try:
        for i in range(len(numbers)):
            try:
                per_sum += numbers[i]
                result += 1

            except TypeError:
                print(f"Не корректный тип данных - {numbers[i]}")
    except TypeError:
        print("В numbers записан некорректный тип данных")
        





def calculate_average(numbers):
    personal_sum(numbers)
    try:
        avg = per_sum / result
        return avg
    except ZeroDivisionError:
        return 0






print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

