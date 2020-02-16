"""
    dodawanie dwoch slownikow
"""


def add_dict(dict1: dict, dict2: dict) -> dict:
    '''Sposob 1
    dict3 = {}
    for key, value in dict1.items():
        dict3[key] = value
    for key, value in dict2.items():
        dict3[key] = value
    return dict3'''

    '''Sposob 2
    dict3 = dict1.copy()
    dict3.update(dict2)
    return dict3'''

    '''Sposob 3'''
    return {**dict1, **dict2}


a = {1:1}
b = {2:2}
c = add_dict(a, b)  # c = {1:1, 2:2}
print(c)