"""
    obliczanie najmniejszej wspolnej wielokrotnosci
"""


def nww(m: int, n: int) -> int:

    c = m*n

    while m != n:
        if m > n:
            m -= n
        else:
            n -= m

    NWW = c // n

    return NWW


print(nww(8, 6))