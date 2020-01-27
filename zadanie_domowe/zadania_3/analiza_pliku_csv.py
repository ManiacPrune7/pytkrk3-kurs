"""
    Zadanie bedzie polegalo na analizie pliku male_oscars.csv.
    Wczytaj plik csv i wykonaj ponizsze zadania:
    a) napisz funkcje, ktora zwroci imie i nazwisko najstarszego zdobywcy oskara z tej listy (kolumna year),
    b) napisz funkcje, ktora posortuje zdobywcow oskara od najstarszego do najmlodszego,
    c) napisz funkcje, ktora doda nowy wiersz do pliku: powinna ona przyjmowac tylko rok, imie i nazwisko zwyciezcy
    oraz tytul filmu - indeks powinien byc ustalany automatycznie.
    Zabezpiecz program na wypadek gdyby argument filename byl sciezka do nieistniejacego pliku. Użyj bloków
    try-except w każdej funkcji.
"""


def get_name_of_the_oldest_winner(filename: str) -> str:
    """Wyciaga imie i nazwisko najstarszego zwyciezcy oskarow.

    :param filename: sciazka do pliku.
    :return: imie i nazwisko najstarszego zwyciezcy jako string
    """
    pass


def sort_oscar_winners_due_to_age(filename: str) -> list:
    """Sortuje liste zwyciezcow wedlug ich wieku - od najstarszego do najmlodszego.

    :param filename: sciazka do pliku.
    :return: posortowana lista.
    """
    pass


def add_new_winner(filename: str):
    """Dodaje nowy wiersz do pliku .csv.

    :param filename: sciazka do pliku.
    """
    pass
