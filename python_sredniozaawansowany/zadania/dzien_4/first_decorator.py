"""
    Pierwszy dekorator.

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


def print_author(function: Callable) -> Callable:  # function = hello_world

    def wrapper():
        print("Autor: JA")
        function()
        # return None

    return wrapper


def hello_world():
    print("Hello, World!")
    # return None


def goodbye_world():
    print("Goodbye, World!")


# print(hello_world())
# print(hello_world)
hello_world()
goodbye_world()
hello = print_author(hello_world) # hello_world = wrapper
goodbye = print_author(goodbye_world)  # goodbye_world = wrapper
hello_world()
goodbye_world()

print("Udekorowane: ")
hello()
goodbye()

# print_author(hello_world)()


# hello_world()

