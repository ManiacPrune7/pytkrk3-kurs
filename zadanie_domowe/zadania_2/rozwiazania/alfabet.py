"""
    Napisz funkcje, ktora poprosi o liczbe, a w zamian zwroci liste
    z tyloma pierwszymi liczbami alfabetu.
    Pomocna bedzie tutaj tablica ascii oraz wbudowane funkcje ord() oraz chr().
    Przyklad:
    >> x = get_alphabet_signs(5)
    >> print(x)
    ["A", "B", "C", "D", "E"]
"""

# Przykladowe rozwiazanie 1: korzytamy z tablicy ascii i rzutowania znaku na liczbę


def get_alphabet_signs(sings_amount: int) -> list:
    """Ustala <signs_amount> pierwszych liczb alfabetu.

    :param sings_amount: liczba naturalna <0; 26>.
    :returns: lista stringow duzych liter, ich ilosc zalezy od parametru signs_amount.

    """
    start_number = ord("A")
    alphabet = []

    for sign in range(start_number, start_number+sings_amount):
        alphabet.append(chr(sign))

    return alphabet


# Przykladowe rozwiazanie 2: korzystamy z modulu string

import string


def get_alphabet_signs(sings_amount: int) -> list:
    """Ustala <signs_amount> pierwszych liczb alfabetu.

    :param sings_amount: liczba naturalna <0; 26>.
    :returns: lista stringow duzych liter, ich ilosc zalezy od parametru signs_amount.

    """
    return list(string.ascii_uppercase[:sings_amount])


# Przykladowe rozwiazanie 3: tworzymy recznie liste A-Z (srednie rozwiazanie, ale dziala)


def get_alphabet_signs(sings_amount: int) -> list:
    """Ustala <signs_amount> pierwszych liczb alfabetu.

    :param sings_amount: liczba naturalna <0; 26>.
    :returns: lista stringow duzych liter, ich ilosc zalezy od parametru signs_amount.

    """
    alphabet = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]

    return alphabet[:sings_amount]


# Przykladowe rozwiazanie 4: tworzymy recznie stringa A-Z (srednie rozwiazanie, ale dziala)


def get_alphabet_signs(sings_amount: int) -> list:
    """Ustala <signs_amount> pierwszych liczb alfabetu.

    :param sings_amount: liczba naturalna <0; 26>.
    :returns: lista stringow duzych liter, ich ilosc zalezy od parametru signs_amount.

    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    return list(alphabet[:sings_amount])



