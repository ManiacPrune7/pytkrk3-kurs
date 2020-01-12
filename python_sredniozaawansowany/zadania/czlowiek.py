"""
    reprezentacja czlowieka
"""


class Czlowiek:
    """
    Klasa reprezentuje czlowieka.
    imie: str
    wiek: int
    hobbies: list, set, tuple
    pensja: int, float
    """
    LICZBA_LUDNOSCI = 0
    def __init__(self, imie, wiek, hobbies, pensja):
        self.imie = imie
        self.__wiek = wiek
        self.hobby = hobbies
        self.pensja = pensja
        self.zdolnosc_kredytowa = self.pensja > 5000  # True or False
        Czlowiek.LICZBA_LUDNOSCI += 1
        self.energia = 100

    def zdobadz_podwyzke(self, procent):

        self.pensja = self.pensja * (100 + procent)/100

    def biegaj(self):
        self.energia -= 20

    def jedz(self):
        print(f"WIEK: {self.__wiek}")
        self.energia += 10

    def zdobadz_hobby(self, hobby):
        self.hobby.append(hobby)


john = Czlowiek("John", 30, ["wedkarstwo"], 2600)
bob = Czlowiek("Bob", 40, ["tkactwo"], 2800)
print(bob._Czlowiek__wiek)  # CIEKAWOSTKA - jedyny sposob zeby dostac sie do zmiennej prywatnej
                            # na zewnatrz
bob.jedz()
print(bob.zdolnosc_kredytowa)
print(Czlowiek.LICZBA_LUDNOSCI)