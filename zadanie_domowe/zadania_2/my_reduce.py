"""
    Napisz wlasna definicje funkcji reduce, ktora powinna dzialac dokladnie tak samo jak funkcja wbudowana
    o tej samej nazwie.
    Zadanie polega na napisaniu funkcji o nazwie my_reduce przyjmujacej dwa argumenty:
    1) funkcji, ktora zostanie wykonana w ciele funkcji my_reduce; ta funkcja bedzie przyjmowala dwa argumenty:
    dwa kolejne elementy listy, w wyniku jej wywolania stana sie jednym i tak az do konca listy,
    w wyniku czego lista zostanie zredukowana do jednego elementu,
    2) listy ktorej elementy maja zostac zredukowane do jednego elementu.
    Twoja funkcje powinno dac sie wywolac tak jak wbudowana, przy czym powinna ona zwracac jedna wartosc (int, str,
    float, itd).
    Przyklad wywolania:
    >> suma = my_reduce(lambda x, y: x+y, [1, 2, 3, 4])
    >> print(suma)
    10
"""

from typing import Callable


def my_reduce(func: Callable, my_list: list):
    """Wlasna definicja funkcji reduce.

    :param func: funkcja dwuargumentowa redukujaca liste do jednego elementu.
    :param my_list: lista, ktora powinna zostac zredukowana do jednego elementu.
    :return: pojedyncza wartosc (int, str, float, etc)

    """
    pass
