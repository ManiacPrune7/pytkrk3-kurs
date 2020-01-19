"""
    pokaz dzialania slowka yield w generatorze
"""


def wznowienia():
    print("wstrzymuje dzialanie")
    yield 1
    print("wznawiam dzialanie")

    print("wstrzymuje dzialanie")
    return 2
    print("wznawiam dzialanie")


for i in wznowienia():
    print(f"Zwrocono wartosc: {i}")