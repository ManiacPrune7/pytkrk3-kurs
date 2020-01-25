"""
    obsluga bledow starym sposobem
"""


def podaj_imie(imie: str):
    if type(imie) is str:
        print(imie)
    else:
        print("Blad!!! imie musi byc stringiem!!")
        return -1

x = podaj_imie(1)
print(x)