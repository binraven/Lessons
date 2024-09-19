"""
Домашнее задание по уроку "Try и Except".
# Modul_8_1
"""



def add_everything_up(a, b):
    try:
        summa = round(a + b, 3)
    except:

        summa = str(a) + str(b)

    return summa


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))












