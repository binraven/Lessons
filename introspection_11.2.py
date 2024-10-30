import inspect
from pprint import pprint


def introspection_info(obj):
    dict_info = {"type": type(obj), 'attributes': dir(obj),  'module': inspect.getmodule(obj)}
    return dict_info


number_info = introspection_info(42)
pprint(number_info)





