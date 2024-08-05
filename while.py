# "Стиль кода часть II. Цикл While."

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
list_index = 0
while my_list[list_index] >= 0:

    if list_index != len(my_list)-1:
        if my_list[list_index] == 0:
            list_index = list_index + 1
            continue
        else:
            print(my_list[list_index])
            list_index = list_index + 1
        continue
    else:
        break

print("Закончился список или мы дошли до 1 не положительного числа")