# "Пространство имён"

calls = 0


def count_calls():
    global calls
    calls += 1

def string_info (str_in):
    str_out = ()
    list_out = [len(str_in), str_in.upper(), str_in.lower()]
    str_out += tuple(list_out)
    count_calls()
    return str_out

def is_contains (str_search, list_search):
    flag_ = None
    for i in range(len(list_search)):
        str_temp = list_search[i]
        if str_search.lower() == str_temp.lower():
            flag_ = True
        else:
            flag_ = False
    count_calls()
    return flag_



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)
