"""
    Napisz funkcje symulujaca rzuty kostka szescioscienna.
    Parametr number_of_throws mowi, ile razy nalezy wykonac losowanie
    (czyli rzucenie koscia do gry). Funkcja zasymuluje gre, po czym
    powinna zwrocic najczesciej wylosowywana liczbe.
    Na potrzeby symulacji mozna wykorzystac modul random i jego funkcje
    randint. Zachecam do przejrzenia dokumentacji.
"""

# Przykladowe rozwiazanie 1: korzytamy z dobrodziejstw Pythona

import random


def get_most_common_number(number_of_throws):
    """Symuluje rzuty kostka i zwraca najczesciej pojawiajaca sie liczbe.

    :param number_of_throws: liczba rzutow kostka do wykonania.
    :returns: najczesciej pojawiajaca sie liczba (int; od 1 do 6)

    """
    results = []

    for _ in range(number_of_throws):
        result = random.randint(1, 6)
        results.append(result)

    most_common_number = results[0]
    for result in results:
        if results.count(result) > results.count(most_common_number):
            most_common_number = result

    return most_common_number

