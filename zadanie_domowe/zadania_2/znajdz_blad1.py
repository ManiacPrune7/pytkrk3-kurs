"""
    Twoim zadaniem jest znalezienie bledu w napisanej funkcji.
    Funkcja powinna zwrocic najmniejszy element w liscie liczb, jednakze
    nie robi tego w 100% poprawnie.
    Przejrzyj jej cialo i zastanow sie, gdzie zostal popelniony blad.
    Mozna zmienic tylko jedna linijke. W funkcji nie brakuje niczego,
    nie ma potrzeby pisac nowych linii kodu.
    Funkcje proponuje przetestowac na zbiorach:
    a = [4, 2, 0, 5, 11, 9, 2]
    b = [-5, 3, 2, -1, 9]
    c = [1, 6, -2, 8, 10, -3]
"""


def compute_the_lowest_value(numbers):
    ans = 0
    for i in range(1, len(numbers)):
        if numbers[i] < ans:
            ans = numbers[i]
    return ans
