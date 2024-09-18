"""
Цель: Закрепить знания о позиционировании в файле, использовав метод tell() файлового объекта. Написать усовершенствованную функцию записи.

Задача "Записать и запомнить":

#module_7_2
"""


def custom_write(file_name, strings):
    file = open(file_name, "w", encoding="utf-8")
    str_number = 1
    strings_positions = {}
    for i in strings:
        strings_positions[(str_number, file.tell())] = i
        file.write(f"{i}\n")
        str_number += 1
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]


result = custom_write('test.txt', info)
for elem in result.items():
  print (elem)
