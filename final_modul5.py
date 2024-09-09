#Задание "Свой YouTube":
#module5hard.py

from time import sleep

class User:

    user_database = {}
    def __init__(self, name, pwd, age):
        self.nickname = name
        self.password = hash(str(pwd))
        self.age = age
        self.user_database[name] = {"nickname": self.nickname, "password": self.password, "age": self.age}
        UrTube.user_list.append(self.nickname)



class Video:
    video_database = {}
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
        self.video_database[title] = {
                                      "title": self.title,
                                      "duration": self.duration,
                                      "time_now": self.time_now,
                                      "adult_mode": self.adult_mode
                                        }




class UrTube:
    current_user = None
    user_list = []
    video_list = []

    def add (self, *args):
        for i in args:
            self.video_list.append(i.title)

    def get_videos(self, zapros):
        for i in self.video_list:
            str_video = str(i)
            str_search = str(zapros)
            if str_search.lower() in str_video.lower():
                print(str_video)
    def watch_video (self, title):
        if self.current_user == None:
            print ("Войдите в аккаунт, чтобы смотреть видео")
        else:
            for i in Video.video_database.keys():
                if title == i:
                    if Video.video_database[i]["adult_mode"] and User.user_database[self.current_user]["age"] < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    else:
                       for y in range(Video.video_database[i]["duration"]):
                           print(y + 1)
                           sleep(1)
                       print("Конец видео")






    def register(self, name, pwd, age):
        if len(self.user_list) == 0:
            new_user = User(name, pwd, age)
            self.current_user = name
        elif name in self.user_list:
            print(f"Пользователь {name} уже существует")
        else:
            self.current_user = name
            new_user = User(name, pwd, age)
    def log_out(self):
        self.current_user = None

    def log_in(self, name, pwd):
        for i in User.user_database.keys():
            if name == i and User.user_database[i]["password"] == hash(str(pwd)):
                self.current_user = name
                print(f"{name}, Добро пожаловать online")






ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
print("Тут просто тестирую метод log_in()")
ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')