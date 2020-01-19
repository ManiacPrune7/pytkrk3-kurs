"""
    generacja nowej listy kwadratow liczb za pomoca:
    a) petli for
    b) list comprehension
    c) map i lambdy
"""

from typing import List

# a)

def for_squares(numbers: List[int]) -> List[int]:
    squares = []
    for number in numbers:
        squares.append(number**2)
    return squares


# b)

def comprehension_squares(numbers):
    return [number**2 for number in numbers]


# c)

# def count_square(number: int) -> int:
#     return number ** 2


def map_squares(numbers):
    squares = map(lambda x: x**2, numbers)
    return list(squares)


x = list(range(10))

print(for_squares(x))
print(comprehension_squares(x))
print(map_squares(x))
