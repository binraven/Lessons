import os
import time

directory = "."


for i in os.walk(directory):
    file_list = i[2]
    abs_path = i[0]
    for file in file_list:
      formatted_time = time.strftime("%d.%m.%Y %H:%M",
                                     time.localtime(os.stat(os.path.join(abs_path, file)).st_mtime))
      print(f"Обнаружен файл: {file}, Путь: {os.path.join(abs_path, file)}, "
            f"Размер: {os.stat(os.path.join(abs_path, file)).st_size} байт, "
            f"Время изменения: {formatted_time}, Родительская директория {abs_path} ")
