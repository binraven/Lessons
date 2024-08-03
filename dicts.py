# "Словари и множества"
my_dict = {"Alex": 26, "Misha":30, "Pasha": 15}
print(my_dict)
print(my_dict["Misha"])
print(my_dict.get("Igor"))

my_dict.update({'Olga': 13, 'Igor': 14})

print(my_dict.pop("Olga"))
print(my_dict)

my_set = {1, 1, 1, 2, 6, 6, "Petr"}
print(my_set)
my_set.update({600, 700})

my_set.discard("Petr")
print(my_set)
