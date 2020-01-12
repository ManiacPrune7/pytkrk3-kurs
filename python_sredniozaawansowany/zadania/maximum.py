"""
    znajduje maksymalna wartosc w liscie
"""


def find_maximum(numbers):
    temp = numbers[0]

    for number in numbers[1:]:
        if number > temp:
            temp = number

    return temp

print(find_maximum([4,2,8,1,9]))