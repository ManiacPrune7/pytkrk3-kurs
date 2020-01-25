"""
    Drugi dekorator.
    Dekorowanie funkcji z argumentami.

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


def print_author(function: Callable) -> Callable:

    def wrapper(*args, **kwargs):
        print("Autor: JA")
        function(*args, **kwargs)  # hello()
        # return None

    return wrapper


def hello(name1, name2):
    print(f"Siemanko, {name1} i czolem {name2}")


hello("Kupidyn", "Kunegunda")
hello = print_author(hello)  # hello = wrapper
hello("Kupidyn", "Marysia")

