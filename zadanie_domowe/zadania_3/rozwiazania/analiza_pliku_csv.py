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

import csv

YRS_OLD_COLUMN = 3
NAME_COLUMN = 4


# Przykladowe rozwiazania - w oparciu o srednio poprawny format
# zadania mozna bylo rowniez wykonac wczesniej "naprawiajac" plik i nadpisujac go
# z poprawnymi wartosciami (tj. bez spacji i "")
# podany plik do grupowania nie uzywa znaku ", tylko '

def get_name_of_the_oldest_winner(filename: str) -> str:
    """Wyciaga imie i nazwisko najstarszego zwyciezcy oskarow.

    :param filename: sciazka do pliku.
    :return: imie i nazwisko najstarszego zwyciezcy jako string
    """
    try:
        with open(filename) as csv_file:

            reader = csv.reader(csv_file, delimiter=",")
            oldest_person = None
            oldest_person_age = 0

            for i, row in enumerate(reader):
                if i == 0:
                    continue  # pominiece wiersza z nazwami kolumn

                yrs_old = int(row[YRS_OLD_COLUMN-1].strip())  # formatowanie wadliwego pliku (spacje, cudzyslowy itd)
                if yrs_old > oldest_person_age:
                    oldest_person_age = yrs_old
                    name = row[NAME_COLUMN-1].strip(' "')
                    oldest_person = name  # uciecie spacji i cudzyslowow

            return oldest_person
    except FileNotFoundError:
        print(f"File  {filename} doesn't exist!")


def sort_oscar_winners_due_to_age(filename: str) -> list:
    """Sortuje liste zwyciezcow wedlug ich wieku - od najstarszego do najmlodszego.

    :param filename: sciazka do pliku.
    :return: posortowana lista.
    """
    badly_formatted_age_column_name = ' "Age"'
    try:
        with open(filename) as csv_file:
            csvreader = csv.DictReader(csv_file)
            winners = []

            for row in csvreader:
                winners.append(row)

            winners.sort(key=lambda x: int(x[badly_formatted_age_column_name].strip()))
            return winners
    except FileNotFoundError:
        print(f"File  {filename} doesn't exist!")

def add_new_winner(filename: str):
    """Dodaje nowy wiersz do pliku .csv.

    :param filename: sciazka do pliku.
    """
    try:
        with open(filename, "r+", newline="") as csv_file:

            my_reader = csv.DictReader(csv_file)

            winners = []
            for game in my_reader:
                winners.append(game)

            last_index = len(winners)
            # Przyklad pobrania danych, mozna to zrobic rowniez poprzez argumenty
            year = " " + input("Year: ")
            age = " " + input("Age: ")
            name = f' "{input("Name: ")}"'
            movie = f' "{input("Movie: ")}"'

            my_writer = csv.writer(csv_file, delimiter=",", quoting=csv.QUOTE_MINIMAL, quotechar="'")
            my_writer.writerow([int(last_index) + 1, year, age, name, movie])
    except FileNotFoundError:
        print(f"File  {filename} doesn't exist!")
