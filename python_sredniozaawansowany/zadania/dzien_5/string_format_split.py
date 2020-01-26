"""
    funkcja wyszukujaca nazwisko z stringu o podanym formacie
"""


def find_surname(string: str) -> str:
    return string.split("nazwisko: ")[1].split(",")[0]


print(find_surname("imie: Jan, nazwisko: Marian, wiek: 32"))
