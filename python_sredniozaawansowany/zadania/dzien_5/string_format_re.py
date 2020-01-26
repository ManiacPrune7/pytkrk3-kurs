"""
    wyszukiwanie nazwiska ze stringa z wykorzystaniem regex
"""

import re


def find_surname(string: str) -> str:

    match = re.match(r"^imie: (\w+), nazwisko: (\w+), wiek: (\d{1,3})$", string)

    if match is not None:
        surname = match.group(2)
        return surname
    else:
        print("BLEDNY FORMAT!!!!")


print(find_surname("imie: Jan, nazwisko: Kowalski, wiek: 33"))
