"""
    Napisz program, który wyszuka slowo zapisane pomiędzy ciągiem liczb.
    Funkcja powinna przyjmowac ciag znakow, a zwracac napis zawarty pomiedzy
    liczbamy w tym ciagu.
    Zadanie nalezy wykonac na dwa sposoby: za pomoca wbudowanych struktur, funkcji Pythona
    oraz z wykorzystaniem modulu re - czyli z wyrazeniami regularnymi.
    Przykladowe ciągi znakow, ktore mozna wykorzystac do testow:
    - 123456NAPIS7890 (odpowiedz: NAPIS)
    - 000000kolejnynapis000000 (odpowiedz: kolejnynapis)
    - innyNAPIS123456789 (odpowiedz: innyNAPIS)
    - 123JESZCZEinnyNAPIS00 (odpowiedz: JESZCZEinnyNAPIS)
"""

import re


def find_word(signs: str) -> str:
    """Znajduje wyraz miedzy ciagiem liczb.

    :param signs: ciag znakow z cyframi oraz jednym napisem wewnatrz.
    :return: wyciagniety wyraz
    """
    found_string = ""

    for sign in signs:
        if sign.isdigit():
            if found_string:
                break
            else:
                continue
        else:
            found_string += sign

    return found_string



def find_word_regex(signs: str) -> str:
    """Znajduje wyraz miedzy ciagiem liczb (wersja z regexem - wyrazeniem regularnym).

    :param signs: ciag znakow z cyframi oraz jednym napisem wewnatrz.
    :return: wyciagniety wyraz
    """
    found_string = ""
    match = re.match(r"\d*([A-Za-z]+)\d*", signs)

    if match is not None:
        found_string = match.group(1)

    return found_string
