"""
Цель: применить на практике оператор with, вспомнить написание кода в парадигме ООП.

Задача "Найдёт везде":

#module_7_3
"""
exclude = [',', '.', '=', '!', '?', ';', ':', ' - ','\n']
get_all_words = {}
find_word = "TexT"
find_dict = {}
count_dict = {}


class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        for i in self.file_names:
            str_name = i
            with open(str_name, encoding="utf-8") as file:
                get_all_words_list = []
                for line in file:
                    s = ''.join(ch for ch in line if ch not in exclude)
                    get_all_words_list.extend(s.lower().split(" "))
            get_all_words[str_name] = get_all_words_list
        return get_all_words

    def find(self, word):
        for key, value in get_all_words.items():
            for i in range (len(value)):
                if word.lower() == value[i]:
                    find_dict[key] = i+1
                    break
        return find_dict

    def count(self, word):
        for key, value in get_all_words.items():
            count_dict[key] = value.count(word.lower())
        return count_dict




finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
