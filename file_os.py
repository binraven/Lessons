import os
import time

directory = "."


for root, dirs, files in os.walk(directory):
    for file in files:

        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(os.stat(file).st_mtime))
        print(f"Обнаружен файл: {file}, Путь: {os.path.join(root, file)}, Размер: {os.stat(file).st_size} байт, "
              f"Время изменения: {formatted_time}, Родительская директория {root} ")