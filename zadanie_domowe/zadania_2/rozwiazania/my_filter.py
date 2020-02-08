"""
    Napisz wlasna definicje funkcji filter, ktora powinna dzialac dokladnie tak samo jak funkcja wbudowana.
    Zadanie polega na napisaniu funkcji o nazwie my_filter przyjmujacej dwa argumenty:
    1) funkcje odfiltrowujaca przyjmujaca tylko jeden argument, zwracajacej albo True, albo False
    2) listy ktora bedzie odfiltrowywana z wartosci.
    Twoja funkcje powinno dac sie wywolac tak jak wbudowana, przy czym powinna ona zwracac nowa liste,
    a nie generator.
    Przyklad wywolania:
    >> new_list = my_filter(lambda x: x>0, [-3, -2, -1, 0, 1, 2, 3])
    >> print(new_list)
    [1, 2, 3]
    Stworz wewnatrz funkcji my_filter tymczasowa liste i w zaleznosci od wyniku wywolania funkcji bedacej jej
    pierwszym argumentem, dodaj element starej listy do nowej listy lub nie.
"""

from typing import Callable


# Przykladowe rozwiazanie 1: uzycie listy skladanej

def my_filter(func: Callable, my_list: list) -> list:
    """Wlasna definicja funkcji filter.

    :param func: funkcja jednoargumentowa odfiltrowujaca, do uzycia wewnatrz naszej funkcji.
    :param my_list: lista do odfiltrowania.
    :return: lista po odfiltrowaniu.

    """
    return [element for element in my_list if func(element)]


# Przykladowe rozwiazanie 2: uzycie listy tymczasowej jako zmiennej pomocniczej

def my_filter(func: Callable, my_list: list) -> list:
    """Wlasna definicja funkcji filter.

    :param func: funkcja jednoargumentowa odfiltrowujaca, do uzycia wewnatrz naszej funkcji.
    :param my_list: lista do odfiltrowania.
    :return: lista po odfiltrowaniu.

    """
    new_list = []
    for elem in my_list:
        if func(elem):
            new_list.append(elem)

    return new_list
