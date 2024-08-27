#"Пространство имен." модуль 4_2
def test_function(*args):
    def inner_function (*args):
        print("Я в области видимости функции test_function")
    inner_function()

test_function()
# inner_function()
# Traceback (most recent call last):
#   File "D:\MyPyLessons\Lessons\name_space_m4.py", line 7, in <module>
#     inner_function()
#     ^^^^^^^^^^^^^^
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
