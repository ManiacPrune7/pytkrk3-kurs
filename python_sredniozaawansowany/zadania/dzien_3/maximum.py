"""
    wlasna implementacja funkcji max z kluczem
"""

from typing import List, Any, Callable

def add(x,y):
    return x+y

# Callable[[int, int], int]


def maximum(iterable: List[Any], key: Callable[[Any], Any] = lambda x: x) -> Any:
    temp = iterable[0]

    for element in iterable:
        if key(temp) < key(element):
            temp = element

    return temp


print(maximum([1, 4, 8, 2, 0]))

strings = ["az", "abcd", "adc", "ab"]
print(maximum(strings, lambda x: x[-1]))