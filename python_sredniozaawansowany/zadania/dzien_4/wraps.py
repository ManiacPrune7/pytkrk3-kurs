"""
    atrybuty funkcji po opakowaniu
"""
from typing import Callable
from functools import wraps


def print_author(function: Callable) -> Callable:

    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Autor: JA")
        result = function(*args, **kwargs)
        return result

    return wrapper

# @print_author
def hello_world():
    """wypisuje napis hello world"""
    print("Hello, World!")

# hello_world()
print(hello_world.__module__)
print(hello_world.__doc__)
print(hello_world.__name__)

hello_world = print_author(hello_world)  # wrapper kitra sie w hello_world

print(hello_world.__module__)
print(hello_world.__doc__)
print(hello_world.__name__)