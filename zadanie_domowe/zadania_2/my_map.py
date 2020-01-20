"""
    Napisz wlasna definicje funkcji map, ktora powinna dzialac dokladnie tak samo jak funkcja wbudowana
    o tej samej nazwie.
    Zadanie polega na napisaniu funkcji o nazwie my_map przyjmujacej dwa argumenty:
    1) funkcje, ktora zostanie wykonana w ciele funkcji my_map na kazdym elemencie listy, wynik powinien zostac
    dodany do nowej listy (ta funkcja wymagac bedzie jednego argumentu),
    2) listy ktorej elementy maja zostac przeksztalcone za pomoca funkcji podanej jako pierwszy argument.
    Twoja funkcje powinno dac sie wywolac tak jak wbudowana, przy czym powinna ona zwracac nowa liste,
    a nie generator.
    Przyklad wywolania:
    >> new_list = my_map(lambda x: x+1, [1, 2, 3, 4])
    >> print(new_list)
    [2, 3, 4, 5]
    Stworz wewnatrz funkcji my_map tymczasowa liste i po wywolaniu funkcji (podanej jako pierwszy argument)
    na kazdym elemencie listy, dodaj tak przetworzony element do nowej listy.
"""

from typing import Callable


def my_map(func: Callable, my_list: list) -> list:
    """wlasna definicja funkcji map.

    :param func: funkcja jednoargumentowa wykonujaca akcje na kazdym elemencie listy my_list.
    :param my_list: lista ktorej kazdy element zostanie argumentem funkcji func.
    :return: lista ze zmienionymi elementami

    """
    pass
