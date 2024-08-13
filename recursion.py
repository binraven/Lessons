# "Рекурсия"

def get_multiplied_digits(n):
    str_number = str(n)

    if len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        first = int(str_number[0])

    return first

result = get_multiplied_digits(40203)
print(result)


