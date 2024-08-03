# "Неизменяемые и изменяемые объекты. Кортежи"

immutable_var = 1, "Привет", [22, 22]
print(immutable_var)

#immutable_var [0]= 1 Числа и строки не изменяемые элементы кортежа. Изменить только можно список внутри кортежа
#print(immutable_var)

mutable_list = [1, "Привет", 100]
mutable_list[2] = 200
print(mutable_list)