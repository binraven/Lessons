# "Распаковка позиционных параметров".

print("1.Функция с параметрами по умолчанию:\n //////////////////////////////\n")
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

print("\n2.Распаковка параметров:\n //////////////////////////////")

values_list = [True, 45, [1,3,4]]
values_dict = {"a" : False, "b" : 245, "c" : "Я словарь"}

print_params(*values_list)
print_params(**values_dict)

print("\n3.Распаковка + отдельные параметры:\n //////////////////////////////")
values_list_2 = ['I am string', [True, False]]
print_params(*values_list_2, 42)

