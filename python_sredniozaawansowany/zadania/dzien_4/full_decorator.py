"""
    Czwarty dekorator.
    Pelne zastosowanie

    Funkcja
    wynik działania:
    Autor: JA
    ...

    1. definicja funkcji, ktora chcemy opakowac (udekorowac)
    2. Dekorator - print_author:
    - funkcja
    - powinna przyjmowac inna funkcja jako argument
    - powinna definiowac funkcje wewnetrzna
    - powinna zwracac funkcje wewnetrzna, ktora dekoruje funkcje podana jako arugment
"""

from typing import Callable


def print_author(function: Callable) -> Callable:  # function = add

    def hello(*args, **kwargs):
        print("NO ELOO")

    def wrapper(*args, **kwargs):
        print("Autor: JA")
        result = function(*args, **kwargs)  # add(*args, **kwargs)
        return result

    return wrapper, hello


@print_author  # add = print_author(add)
def add(a: int, b: int) -> int:
    return a + b


print(add(3, 5))
print(add(7, 5))
