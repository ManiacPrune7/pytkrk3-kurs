"""
    odfiltrowywanie list
"""


def filter_for(strings):
    temp = []
    for string in strings:
        if len(string) <= 3:
            temp.append(string)
    return temp


def filter_comprehension(strings):
    return [string for string in strings if len(string) <= 3]


def filter_filter(strings):
    return list(filter(lambda string: len(string) <= 3, strings))


napisy = ["abc", "adfsfdg", "asdsadasdsa", "a"]
print(filter_for(napisy))
print(filter_comprehension(napisy))
print(filter_filter(napisy))