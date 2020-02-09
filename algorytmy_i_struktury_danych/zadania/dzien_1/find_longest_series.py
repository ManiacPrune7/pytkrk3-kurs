"""
    znajduje najdluzszy ciag tych samym liter nastepujacy  po sobie
"""


def find_longest_series(string: str) -> str:
    longest_letter = ""
    len_longest = 0
    previous_letter = ""
    len_current = 0

    for letter in string:
        if letter != previous_letter:
            previous_letter = letter
            len_current = 1
        else:
            len_current += 1

        if len_current > len_longest:
            len_longest = len_current
            longest_letter = previous_letter
    return longest_letter


print(find_longest_series("aaaabbbb"))
