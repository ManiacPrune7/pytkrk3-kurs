"""
    Uruchamianie funkcji trzykrotnie.
"""

from typing import Callable


def thrice(func: Callable):

    def wrapper(*args, **kwargs):
        a = func(*args, **kwargs)
        b = func(*args, **kwargs)
        c = func(*args, **kwargs)
        return c
        # return None

    return wrapper

@thrice
def hello_world():
    print("Hello, World!")

@thrice
def add(a, b):
    print("Dodaje...")
    return a+b

hello_world()
print(add(1, 4))