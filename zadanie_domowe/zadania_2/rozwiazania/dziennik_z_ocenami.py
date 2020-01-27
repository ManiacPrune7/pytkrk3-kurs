"""
    Dla podanego slownika reprezentujacego oceny, napisz 4 funkcje:
    a) pierwsza powinna zwracac liste wszystkich ocen ze slownika,
    b) druga powinna ustalic i zwrocic maksymalna ocene z dziennika,
    c) trzecia ustala ile osob nie zaliczylo przedmiotu (kazda osoba z ocena 2.0),
    d) czwarta powinna zwrocic imie osoby z najwyzsza ocena.
    Przykladowy "dziennik" reprezentuje slownik CLASS_REGISTER.
    Nazwy i parametry funkcji do wlasnego wyboru :)
"""

from typing import List

CLASS_REGISTER = {
    "Ania": 4.0,
    "Jakub": 3.5,
    "Roman": 4.0,
    "Kasia": 4.0,
    "Aneta": 4.5,
    "Wojtek": 2.0,
    "Ola": 2.0,
    "Monika": 3.0,
    "Ula": 5.0,
    "Mikolaj": 4.0,
    "Robert": 3.0
}


def get_all_grades() -> List[float]:
    """Ustala liste wszystkich ocen z dziennika CLASS_REGISTER.

    :return: liste wszystkich ocen.

    """
    return CLASS_REGISTER.values()


def get_best_grade() -> float:
    """Wyciaga najlepsza ocene z dziennika CLASS_REGISTER

    :return: najwyzsza ocena z dziennika.

    """
    return max(CLASS_REGISTER.values())


def get_amount_of_failures() -> int:
    """Ustala liczbe osob, ktore nie zdaly.

    :return: liczba osob jest >= 0

    """
    return len([grade for grade in CLASS_REGISTER.values() if grade < 3.0])


# Przyklad 1


def get_student_with_best_grade() -> str:
    """Ustala imie ucznia z najwyzsza ocena.

    :return: imie ucznia.

    """
    grades = list(CLASS_REGISTER.values())
    students = list(CLASS_REGISTER.keys())
    return students[grades.index(max(grades))]


# Przyklad 2


def get_student_with_best_grade() -> str:
    """Ustala imie ucznia z najwyzsza ocena.

    :return: imie ucznia.

    """
    best_grade = max(CLASS_REGISTER.values())  # lub best_grade = get_best_grade() #  (zdefiniowane wczesniej przez nas)
    best_student = list(filter(lambda x: x[1] == best_grade, CLASS_REGISTER.items()))[0][0]
    return best_student


# Przyklad 3


def get_student_with_best_grade() -> str:
    """Ustala imie ucznia z najwyzsza ocena.

    :return: imie ucznia.

    """
    best_grade = max(CLASS_REGISTER.values())  # lub best_grade = get_best_grade() #  (zdefiniowane wczesniej przez nas)

    for student in CLASS_REGISTER.keys():
        if CLASS_REGISTER[student] == best_grade:
            return student  # jesli znajdziemy takiego studenta, to od razu konczymy petle i wychodzimy z funkcji,
                            # bo po co iterowac dalej jak juz mamy wszystko czego potrzeba
