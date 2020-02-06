"""
    Napisz funkcje szyfrujaca w sposob znany blizej jako szyfr Cezara.
    Szyfr wywodzi sie z czasow imperium rzymskiego, ktore celem dezinformacji w przypadku przechwycenia listu
    przez wrogie oddzialy, szyfrowalo swoje wiadomosci.
    Sposob szyfrowania jest prosty: kazdej literze w wiadomosci przypisuje sie litere o 3 pozycje dalej w alfabecie.
    Stad wiadomosc "ABC" zostalaby zaszyfrowana jako "DEF". Spacje pozostaja spacjami, kropki kropkami,
    znaki przestankowe sie nie zmieniaja - szyfruje sie tylko litery.
    Funkcja szyfruj_cezar powinna przyjmowac jeden argument: stringa z wiadomoscia, a powinna zwracac zaszyfrowany
    string zgodnie z algorytmem.
    Przyklad wywolania:
    >> sekret = szyfruj_cezar("ABC DEF GHI")
    >> print(sekret)
    "DEF GHI JKL"
"""

LETTERS_IN_ALPHABET = 26

# Rozwiazanie przykladowe 1: uzycie ord i chr


def szyfruj_cezar(text: str) -> str:
    """Szyfruje tekst podany jako argument wedlug algorytmu Cezara.

    :param text: string do zaszyfrowania.
    :return: zaszyfrowany tekst.

    """
    cipher = []
    big_letters_range = (65, 90)
    small_letters_range = (97, 122)

    for letter in text:
        if big_letters_range[0] <= ord(letter) <= big_letters_range[1]:
            new_letter = chr((ord(letter)+3-65) % LETTERS_IN_ALPHABET + 65)  # 65 to liczba ascii dla litery "A"
        elif small_letters_range[0] <= ord(letter) <= small_letters_range[1]:
            new_letter = chr((ord(letter)+3-97) % LETTERS_IN_ALPHABET + 97)  # 97 to liczba ascii dla litery "a"
        else:
            new_letter = letter

        cipher.append(new_letter)

    return "".join(cipher)


# Rozwiazanie przykladowe 2: uzycie biblioteki string

import string


def szyfruj_cezar(text: str) -> str:
    """Szyfruje tekst podany jako argument wedlug algorytmu Cezara.

    :param text: string do zaszyfrowania.
    :return: zaszyfrowany tekst.

    """
    cipher = []
    big_letters = list(string.ascii_uppercase)
    small_letters = list(string.ascii_lowercase)

    for letter in text:
        if letter in big_letters:  # lub if letter.isupper()
            new_letter = big_letters[(big_letters.index(letter)+3) % LETTERS_IN_ALPHABET]
        elif letter in small_letters:  # lub if letter.islower()
            new_letter = small_letters[(big_letters.index(letter)+3) % LETTERS_IN_ALPHABET]
        else:
            new_letter = letter

        cipher.append(new_letter)

    return "".join(cipher)
