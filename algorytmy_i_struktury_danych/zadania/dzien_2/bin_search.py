"""
    implementacja wyszukiwania binarnego
"""


def bin_search(a: list, x: int) -> str:

    l = 0
    p = len(a)-1

    while not l > p:
        s = (l+p)//2
        if a[s] == x:
            return f"odnalezione element {x} pod indeksem {s}"
        if a[s] < x:
            l = s + 1
        else:
            p = s - 1
    return f"nie odnaleziono elementu o wartosci {x}"


def find(a, x):
    for element in a:
        if element == x:
            return "znaleziono"
    return "nie ma"

import time
a = time.perf_counter()
print(bin_search([num for num in range(9999999)], 9999998))
b = time.perf_counter()
print(find([num for num in range(9999999)], 9999998))
c = time.perf_counter()
print(b-a, c-b)
