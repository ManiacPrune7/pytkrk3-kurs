"""
    NWD rekurencyjnie
"""


def nwd(a, b):  # nwd(15, 15)
    if a == b:
        return a
    if a > b:
        a = a-b
    elif b > a:
        b = b-a

    return nwd(a, b)

print(nwd(36, 27))