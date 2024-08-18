# Задание "Раз, два, три, четыре, пять .... Это не всё?":

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]


res = []
res_debug = []
def calculate_structure_sum(list):

    for i in list:
        item_type(i)
    return (sum(res))
def res_list(arg):
    global res, res_debug
    res_debug.append(arg)
    print(res_debug)
    if isinstance(arg, str):
        res.append(len(arg))
    else:
        res.append(arg)

def item_counter(args):
    print(f"Я счетчик, на вход я получил {args}")

    if isinstance(args, str) or isinstance(args, int):
        print(f"Я счетчик, хочу посчитать это {args}")
        res_list(args)
    elif isinstance(args, list):
        print(f"Лист в счетчике {args}")
        inner_lister(args)
    else:
        print(f"Нашел структуру для преобразования {i} ")
        inner_lister(i)

def inner_lister(structura):
    print(f"Я внутрренний переборщик, сейчас расчешу {structura}")
    for i in structura:
        item_type(i)
def item_type(item_structure):
    print(f"Принят элемент {item_structure} его тип {type(item_structure)}")
    if isinstance(item_structure, dict):
        print(f"К нам пришел словарь {item_structure}")
        dict_keys = list (item_structure.keys())
        dict_values = list(item_structure.values())
        print(f"Ясловарь разобрал на ключи: {dict_keys} и значения: {dict_values}")
        item_counter(dict_keys)
        item_type(dict_values)
    elif isinstance(item_structure, tuple) or isinstance(item_structure, set):
        print(f"К нам пришел кортеж или множество {item_structure}")
        item_list = list(item_structure)
        print(f"Сделали из этого лист: {item_list}")
        item_counter(item_list)
    else:
        print(f"{item_structure} {type(item_structure)} Видимо это лист, строка или число\nТогда вызываем счетчик ")
        item_counter(item_structure)


result = calculate_structure_sum(data_structure)
print(result)



