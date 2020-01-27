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


def szyfruj_cezar(text: str) -> str:
    """Szyfruje tekst podany jako argument wedlug algorytmu Cezara.

    :param text: string do zaszyfrowania.
    :return: zaszyfrowany tekst.

    """
    pass
