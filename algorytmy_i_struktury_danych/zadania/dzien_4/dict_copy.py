"""
    kopiowanie slownika
"""


def copy_dict(d: dict) -> dict:
    #return {key: value for key, value in d.items()}
    copy_d = {}
    for key, value in d.items(): # [("Ania", 5), ("Kacper", 4.5), ("Zosia", 4)]
        copy_d[key] = value
        print(copy_d)


grades = {"Ania": 5, "Kacper": 4.5, "Zosia": 4}
grades_copy = copy_dict(grades)