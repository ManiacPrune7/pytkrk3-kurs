"""
    zamiana liczby dziesietnej na binarna
"""


def dec_to_bin(d: int) -> str:

    binary = ""

    while d != 0:
        r = d % 2

        if r == 1:
            binary = "1" + binary
        else:
            binary = "0" + binary

        d = d // 2

    return binary

print(dec_to_bin(12))