import inspect
from pprint import pprint


def introspection_info(obj):
    obj_attr_list = []
    obj_method_list = []
    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)
        if inspect.isbuiltin(attr) or inspect.ismethod(attr) or inspect.isfunction(attr):
            obj_method_list.append(attr_name)
        else:
            obj_attr_list.append(attr_name)

    dict_info = {"type": type(obj), 'attributes': obj_attr_list, 'methods': obj_method_list, 'module': inspect.getmodule(obj)}
    return dict_info


number_info = introspection_info(42)
pprint(number_info)





